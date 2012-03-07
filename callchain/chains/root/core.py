# -*- coding: utf-8 -*-
'''callchains root chain mixins'''

from collections import deque

from callchain.octopus import ResetLocalMixin

__all__ = ['RootMixin']


class RootMixin(ResetLocalMixin):

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
