# -*- coding: utf-8 -*-
'''active call chain mixins'''

from collections import deque

from stuf.utils import iterexcept
from octopus.resets import ResetLocalMixin

from callchain.chains.mixins import CLinkMixin, CChainMixin


class _ChainMixin(ResetLocalMixin):

    '''call chain mixin'''

    def __call__(self, *args):
        '''load args into incoming thing'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self._inextend(args)
        return self

    def _setup_chain(self):
        '''setup call chain'''
        # call chain
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

    def chain(self, call, key=False, *args, **kw):
        '''
        add callable or appspaced callable to call chain, partializing it with
        any passed arguments

        @param call: callable or application label
        @param key: callable key label (default: False)
        '''
        self._cappend(self.M.partial(call, key, *args, **kw))
        return self

    _ochain = chain

    def commit(self):
        '''run call chain'''
        # consume call chain till exhausted
        calls = iterexcept(self._chain.popleft, IndexError)
        # put call chain results in outgoing things
        self.outappend(call() for call in calls)
        return self

    _ocommit = commit


class ChainLinkMixin(_ChainMixin, CLinkMixin):

    '''linked call chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(ChainLinkMixin, self).__init__(root)
        # setup call chain
        self._setup_chain()
        # sync with root
        self._inextend(root.incoming)
        # sync outgoing
        self._outextend(root.outgoing)
        # sync callable
        self._call = root._call
        # sync postitional arguments
        self._args = root._args
        # sync keyword arguments
        self._kw = root._kw


class CallChainMixin(_ChainMixin, CChainMixin):

    '''call chain mixin'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(CallChainMixin, self).__init__(pattern, required, defaults, **kw)
        # setup call chain
        self._setup_chain()

    def back(self, link):
        # sync incoming
        self._inclear()
        self._inextend(link.incoming)
        # sync outgoing
        self._outclear()
        self._outextend(link.outgoing)
        # sync callable
        self._call = link._call
        # sync postitional arguments
        self._args = link._args
        # sync keyword arguments
        self._kw = link._kw
        return self

    _oback = back
