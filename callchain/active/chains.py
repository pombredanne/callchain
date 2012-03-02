# -*- coding: utf-8 -*-
'''active call chains'''

from threading import local
from collections import deque

from stuf.utils import iterexcept

from callchain.chains.mixins import ChainLinkMixin, CallChainMixin


class _AChainMixin(local):

    '''base call chain'''

    def __init__(self):
        super(_AChainMixin, self).__init__()
        ## call chain #########################################################
        self._chain = deque()
        # call chain right extend
        self._cxtend = self._chain.extend
        # call chain right append
        self._cappend = self._chain.append
        # call chain left append
        self._cappendleft = self._chain.appendleft
        # call chain left pop
        self._cpopleft = self._chain.popleft
        # call chain clear
        self._cclear = self._chain.clear

    def __call__(self, *args):
        '''
        init

        @param incoming: incoming queue
        @param outgoing: outgoing queue
        '''
        incoming = deque()
        # extend if just one argument
        if len(args) == 1:
            incoming.append(args[0])
        else:
            incoming.extend(args)
        # callable stub
        self._call = None
        # callable postitional arguments stub
        self._args = ()
        # callable keyword arguments stub
        self._kw = {}
        # incoming queue
        self.incoming = incoming
        # outgoing queue
        self.outgoing = deque()
        #######################################################################
        ## incoming things ####################################################
        #######################################################################
        # incoming things right append
        self._inappend = self.incoming.append
        # incoming things left append
        self._inappendleft = self.incoming.appendleft
        # incoming things clear
        self._inclear = self.incoming.clear
        # incoming things right extend
        self._inextend = self.incoming.extend
        # incoming things left extend
        self._inextendleft = self.incoming.extendleft
        #######################################################################
        ## outgoing things ####################################################
        #######################################################################
        # outgoing things right append
        self._outappend = self.outgoing.append
        # outgoing things right extend
        self._outextend = self.outgoing.extend
        # outgoing things clear
        self._outclear = self.outgoing.clear
        # outgoing things right pop
        self.pop = self.outgoing.pop
        # outgoing things left pop
        self.popleft = self.outgoing.popleft
        return self

    def commit(self):
        '''invoke call chain'''
        # consume call chain until exhausted & put results in outgoing things
        calls = iterexcept(self._chain.popleft, IndexError)
        self.outappend(call() for call in calls)
        return self

    def chain(self, call, key=False, *args, **kw):
        '''
        add callable or appspaced application to call chain, partializing it
        with any passed parameters

        @param call: callable or application label
        @param key: key label (default: False)
        '''
        self._cappend(self.M.partial(call, key, *args, **kw))
        return self


class AChainLinkMixin(_AChainMixin, ChainLinkMixin):

    '''linked call chain mixin'''

    def __init__(self, root):
        super(AChainLinkMixin, self).__init__(root)
        # sync with root
        self.extend(root.outgoing)

    def back(self):
        '''return to root call chain'''
        return self.root.clear().extend(self.outgoing)


class ACallChainMixin(_AChainMixin, CallChainMixin):

    '''call chain mixin'''
