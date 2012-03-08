# -*- coding: utf-8 -*-
'''active queued chain mixins'''

from collections import deque

from stuf.utils import iterexcept

from callchain.octopus import Octuplet
from callchain.chains import ChainMixin, RootedQMixin

from callchain.events import ERunMixin, EventMixin, ERootedMixin
from callchain.resets import ResetLocalMixin


class ActiveMixin(ChainMixin):

    '''active chain execution mixin'''

    def commit(self):
        '''consume call chain until exhausted'''
        self._outextend(
            c() for c in iterexcept(self._chain.popleft, IndexError)
        )
        return self

    _ocommit = commit


class ActiveEMixin(ERunMixin):

    '''active queued event chain mixin'''

    def fire(self, *events):
        '''run calls bound to `*events` NOW'''
        try:
            # clear scratch queue
            self._sclear()
            # queue global and local bound callables
            self._sxtend(self._events(*events))
            # run event call chain until scratch queue is exhausted
            self._outextend(call() for call in iterexcept(
                self._scratch.popleft, IndexError,
            ))
        finally:
            # clear scratch queue
            self._sclear()
        return self


class ActiveRootedMixin(RootedQMixin):

    '''active queue rooted chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(ActiveRootedMixin, self).__init__(root)
        # sync with root incoming things
        self._inextend(root.incoming)
        # sync with root outgoing things
        self._outextend(root.outgoing)


class ActiveChainletMixin(ActiveRootedMixin, Octuplet):

    '''active queued chainlet mixin'''


class ActiveELetMixin(EventMixin, ERootedMixin, ActiveChainletMixin):

    '''active eventlet mixin'''


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
