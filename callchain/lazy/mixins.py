# -*- coding: utf-8 -*-
'''callchain contexts'''

from callchain.queued import ContextMixin
from callchain.reset import ResetLocalMixin
from callchain.linked import LinkedQ, EventLinkQ
from callchain.chainlet import EventletQ, ChainletQ


class LazyContext(ContextMixin):

    '''lazy context manager'''

    def __init__(self, queue):
        '''
        init

        @param queue: queue
        '''
        super(LazyContext, self).__init__(queue)
        self._queue = queue

    def __call__(self, args):
        self._queue._scratch = args

    def iter(self, args):
        self._queue._scratch = iter(args)

    def append(self, args):
        self._queue._scratch = iter([args])

    def __enter__(self):
        # clear scratch queue
        self._queue._scratch = None
        return self

    def __exit__(self, t, v, e):
        # extend incoming items with outgoing items
        self._cxtend(self._scratch)
        # clear scratch _queue
        self._queue._scratch = None


class LazyContextMixin(ResetLocalMixin):

    '''lazy context mixin'''

    @property
    def _callsync(self):
        return LazyContext(self)


class LazyChainlet(ChainletQ, LazyContext):

    '''lazy chainlet'''


class LazyEventlet(EventletQ, LazyContext):

    '''lazy eventlet'''


class LazyLinked(LinkedQ, LazyContext):

    '''lazy linked chain'''


class LazyLinkedEvent(EventLinkQ, LazyContext):

    '''lazy linked event chain'''
