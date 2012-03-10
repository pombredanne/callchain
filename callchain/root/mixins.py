# -*- coding: utf-8 -*-
'''root chains'''

from collections import deque

from callchain.mixin.reset import ResetLocalMixin
from stuf.utils import iterexcept


class RootMixin(ResetLocalMixin):

    '''mixin for standalone chains'''

    def _setup_chain(self):
        '''setup call chain'''
        self._csetup_chain()
        self.outgoing = deque()
        # outgoing things right extend
        self.outextend = self.outgoing.extend
        # outgoing things clear
        self._outclear = self.outgoing.clear
        # outgoing things right append
        self._outappend = self.outgoing.extend

    _rsetup_chain = _setup_chain

    def clear(self):
        '''ANNIHILATE!!!'''
        self._outclear()
        self._cclear()
        return self

    _rclear = clear

    def end(self):
        '''return outgoing things and clear out all things'''
        results = self.pop() if len(
            self.outgoing
        ) == 1 else list(self.outgoing)
        self.clear()
        return results

    _rfinal = end

    def results(self):
        '''yield outgoing things and clear outgoing things'''
        for thing in iterexcept(self.outgoing.popleft, IndexError):
            yield thing

    _rresults = results

    def value(self):
        '''return outgoing things and clear outgoing things'''
        results = self.pop() if len(
            self.outgoing
        ) == 1 else list(self.outgoing)
        self._outclear()
        return results

    _rvalue = value

    def first(self):
        '''first incoming thing'''
        with self._sync as sync:
            sync.append(sync.iterable.popleft())
        return self

    _ofirst = first

    def last(self):
        '''last incoming thing'''
        with self._sync as sync:
            sync.append(sync.iterable.pop())
        return self

    _olast = last
