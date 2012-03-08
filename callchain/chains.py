# -*- coding: utf-8 -*-
'''callchains chain mixins'''

from collections import deque
from functools import partial

from twoq.support import isstring

from callchain.octopus import Octopus
from callchain.octopus import ResetLocalMixin


class ChainsMixin(ResetLocalMixin):

    '''chain mixin'''

    def _setup_chain(self):
        '''setup call chain'''
        _chain = deque()
        # call chain right extend
        self._cxtend = _chain.extend
        # call chain right append
        self._cappend = _chain.append
        # call chain left append
        self._cappendleft = _chain.appendleft
        # call chain left pop
        self._cpopleft = _chain.popleft
        # call chain clear
        self._cclear = _chain.clear
        # call chain
        self._chain = _chain

    _osetup_chain = _setup_chain

    def chain(self, call, key=False, *args, **kw):
        '''
        add callable or appspaced callable to call chain, partializing it with
        any passed arguments

        @param call: callable or application label
        @param key: appspace key label (default: False)
        '''
        if not isstring(call):
            call = partial(call, *(key,) + args, **kw)
        else:
            call = partial(self.M.get(call, key), *args, **kw)
        self._cappend(call)
        return self

    _ochain = chain


class QMixin(ChainsMixin):

    '''chained queue mixin'''

    def clear(self):
        '''ANNIHILATE!!!'''
        self._oclear()
        self._cclear()
        return self

    _cclear = clear

    def tap(self, call, key=False):
        '''
        add call

        @param call: callable or appspace label
        @param key: linked call chain key (default: False)
        '''
        # reset postitional arguments
        self._args = ()
        # reset keyword arguments
        self._kw = {}
        # set current application
        self._call = self._M.get(call, key) if isstring(call) else call
        return self

    _ctap = tap


class RootedMixin(ChainsMixin):

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(RootedMixin, self).__init__(root)
        self._setup_chain()


class RootedQMixin(RootedMixin, QMixin):

    '''linked call chain queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(RootedQMixin, self).__init__(root)
        # sync with root postitional arguments
        self._args = root._args
        # sync with root keyword arguments
        self._kw = root._kw
        # sync with root callable
        self._call = root._call


class ChainMixin(ChainsMixin, Octopus):

    '''call chain mixin'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(ChainMixin, self).__init__(pattern, required, defaults, **kw)
        self._setup_chain()

    def back(self, link):
        '''
        handle return from linked call chain

        @param link: linked call chain
        '''
        self.clear()
        # extend call chain with root call chain
        self._cappend(link._chain)
        return self

    _oback = back


class ChainQMixin(ChainMixin, QMixin):

    '''queued call chain mixin'''

    def back(self, link):
        '''
        handle return from linked call chain

        @param link: linked call chain
        '''
        self._oback(link)
        # sync with link callable
        self._call = link._call
        # sync with link postitional arguments
        self._args = link._args
        # sync with link keyword arguments
        self._kw = link._kw
        return self

    _cback = back
