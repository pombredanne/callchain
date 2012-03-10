# -*- coding: utf-8 -*-
'''root chains'''

from collections import deque

from callchain.mixin.reset import ResetLocalMixin


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

    _cclear = clear
