# -*- coding: utf-8 -*-
#pylint: disable-msg=w0221
'''root chain mixins'''

from collections import deque

from twoq.active.mixins import ResultQMixin


class RootMixin(ResultQMixin):

    '''base root chain mixin'''

    def _setup(self):
        '''setup chain'''
        self.outgoing = deque()
        # outgoing things right extend
        self.outextend = self.outgoing.extend
        # outgoing things clear
        self._outclear = self.outgoing.clear
        # outgoing things right append
        self._outappend = self.outgoing.append
        # outgoing things left pop
        self.popleft = self.outgoing.popleft
        self._c_setup()

    _d_setup = _setup


class RootableMixin(RootMixin):

    '''base rooted root chain mixin'''

    def _setup(self, root):
        '''
        setup chain

        @param root: root object
        '''
        self._d_setup()
        self._r_setup(root)
