# -*- coding: utf-8 -*-
'''active queued mixins'''

from stuf.utils import iterexcept

from callchain.mixin.reset import ResetLocalMixin


class ActiveRootedMixin(ResetLocalMixin):

    '''active queued rooted chain mixin'''

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


class ActiveCallMixin(ResetLocalMixin):

    '''active queued call mixin'''

    def commit(self):
        '''consume call chain until exhausted'''
        self._outextend(
            c() for c in iterexcept(self._chain.popleft, IndexError)
        )
        return self

    _ccommit = commit


class ActiveECallMixin(ActiveCallMixin):

    '''active queued event call mixin'''

    def fire(self, *events):
        '''run calls bound to `events` NOW'''
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
