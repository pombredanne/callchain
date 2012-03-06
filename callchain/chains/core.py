# -*- coding: utf-8 -*-
'''call chains mixins'''

from collections import deque

from stuf.utils import iterexcept

from callchain.octopus import ResetLocalMixin

__all__ = ('LoneMixin', 'QMixin')


class _CoreMixin(ResetLocalMixin):

    '''chain core mixin'''

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
        @param key: key label (default: False)
        '''
        self._cappend(self.M.partial(call, key, *args, **kw))
        return self

    _ochain = chain

    def commit(self):
        '''consume call chain until exhausted'''
        self._outextend(
            call() for call in iterexcept(self._chain.popleft, IndexError)
        )
        return self

    _ocommit = commit


class LoneMixin(_CoreMixin):

    def _setup_chain(self):
        self._osetup_chain()
        self.outgoing = deque()
        # outgoing things right extend
        self._outextend = self.outgoing.extend
        # outgoing things clear
        self._outclear = self.outgoing.clear
        # outgoing things right append
        self._outappend = self.outgoing.extend

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
        isstring = self.port.isstring
        self._call = self._M.get(call, key) if isstring(call) else call
        return self

    _ctap = tap
