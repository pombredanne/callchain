# -*- coding: utf-8 -*-
'''call chains mixins'''

from collections import deque
from functools import partial

from twoq.support import isstring

from callchain.octopus import ResetLocalMixin

__all__ = ('LoneMixin', 'QMixin')


class _CoreMixin(ResetLocalMixin):

    '''core chain mixin'''

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


class LoneMixin(_CoreMixin):

    '''mixin for standalone chains'''

    def _setup_chain(self):
        '''setup call chain'''
        self._osetup_chain()
        self.outgoing = deque()
        # outgoing things right extend
        self._outextend = self.outgoing.extend
        # outgoing things clear
        self._outclear = self.outgoing.clear
        # outgoing things right append
        self._outappend = self.outgoing.extend

    _csetup_chain = _setup_chain

    def clear(self):
        '''ANNIHILATE!!!'''
        self._outclear()
        self._cclear()
        return self

    _cclear = clear


class QMixin(_CoreMixin):

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
