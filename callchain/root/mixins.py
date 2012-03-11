# -*- coding: utf-8 -*-
'''root chain mixins'''

from collections import deque

from twoq.active.mixins import ResultQMixin


class RootMixin(ResultQMixin):

    '''base chain mixin'''

    def _setup_chain(self):
        '''setup chain'''
        self._csetup_chain()
        self.outgoing = deque()
        # outgoing things right extend
        self.outextend = self.outgoing.extend
        # outgoing things clear
        self._outclear = self.outgoing.clear
        # outgoing things right append
        self._outappend = self.outgoing.extend

    _rsetup_chain = _setup_chain
