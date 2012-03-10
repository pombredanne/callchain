# -*- coding: utf-8 -*-
'''lazy queued mixins'''

from collections import deque

from stuf.utils import iterexcept

from callchain.mixin.reset import ResetLocalMixin


class LazyRootedMixin(ResetLocalMixin):

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


class LazyCallMixin(ResetLocalMixin):

    '''lazy queued chain mixin'''

    def commit(self):
        '''consume call chain until exhausted'''
        self.outgoing = deque(
            c() for c in iterexcept(self._chain.popleft, IndexError)
        )
        return self

    _ccommit = commit


class LazyECallMixin(LazyCallMixin):

    '''lazy queued event chain mixin'''

    def fire(self, *events):
        '''run calls bound to `events` NOW'''
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
