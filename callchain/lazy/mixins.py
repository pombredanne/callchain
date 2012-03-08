# -*- coding: utf-8 -*-
'''lazy queued mixins'''

from collections import deque

from stuf.utils import iterexcept

from callchain.octopus import Octuplet
from callchain.chains import RootedQMixin, ChainMixin
from callchain.events import ERunMixin, ERootedMixin, EventMixin


class LazyMixin(ChainMixin):

    '''lazy queued chain mixin'''

    def commit(self):
        '''consume call chain until exhausted'''
        self.outgoing = deque(
            c() for c in iterexcept(self._chain.popleft, IndexError)
        )
        return self

    _ocommit = commit


class ELazyMixin(ERunMixin):

    '''lazy queued event chain mixin'''

    def fire(self, *events):
        '''run calls bound to `*events` NOW'''
        try:
            # clear scratch queue
            self._scratch = None
            # queue global and local bound callables
            self._scratch = deque(self._events(*events))
            # run event call chain until scratch queue is exhausted
            self.outgoing = deque(call() for call in iterexcept(
                self._scratch.popleft, IndexError,
            ))
        finally:
            # clear scratch queue
            self._scratch = None
        return self


class LazyRootedMixin(RootedQMixin):

    '''lazy queued rooted chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(LazyRootedMixin, self).__init__(root)
        # sync with root incoming things
        self.incoming = root.incoming
        # sync with root outgoing things
        self.outgoing = root.outgoing


class LazyChainletMixin(LazyRootedMixin, Octuplet):

    '''lazy queued chainlet mixin'''


class LazyEventletMixin(EventMixin, ERootedMixin, LazyChainletMixin):

    '''lazy eventlet mixin'''
