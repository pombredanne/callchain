# -*- coding: utf-8 -*-
'''lazy queued mixins'''

from collections import deque

from stuf.utils import iterexcept

from callchain.call import ECallingMixin, CallingMixin


class LazyMixin(CallingMixin):

    '''lazy queued chain mixin'''

    def commit(self):
        '''consume call chain until exhausted'''
        self.outgoing = deque(
            c() for c in iterexcept(self._chain.popleft, IndexError)
        )
        return self

    _ocommit = commit


class LazyEMixin(ECallingMixin):

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
