# -*- coding: utf-8 -*-
'''active call chains'''

from threading import local
from collections import deque

from stuf.utils import iterexcept

from callchain.chains.mixins import LinkMixin, EventChainMixin


class _AChainMixin(local):

    '''base call chain'''

    def __call__(self, *args):
        self.clear()
        self._inextend(args)
        return self

    def _setup_chain(self):
        '''setup call chain'''
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


class ChainLinkMixin(_AChainMixin, LinkMixin):

    '''linked call chain mixin'''

    def __init__(self, root):
        super(ChainLinkMixin, self).__init__(root)
        # setup call chain
        self._setup_chain()
        # sync with root
        self._inextend(root.incoming)
        # sync outgoing
        self._outextend(root.outgoing)
        # sync callable
        self._call = root._call
        # sync callable postitional arguments
        self._args = root._args
        # sync callable keyword argumentss
        self._kw = root._kw


class CallChainMixin(_AChainMixin, EventChainMixin):

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
        # sync callable postitional arguments
        self._args = link._args
        # sync callable keyword arguments
        self._kw = link._kw
        return self
