# -*- coding: utf-8 -*-
'''callchain active contexts'''

from callchain.mixin.queued import ContextMixin
from callchain.mixin.reset import ResetLocalMixin
from callchain.assembly.chainlet import EventletQ, ChainletQ
from callchain.assembly.linked import LinkedQ, EventLinkQ

__all__ = ['ActiveContext']


class ActiveContext(ContextMixin):

    '''active context manager'''

    def __init__(self, queue):
        '''
        init

        @param queue: queue
        '''
        super(ActiveContext, self).__init__(queue)
        self._sxtend = queue._sxtend
        self._sappend = queue._sappend
        self._sclear = queue._sclear
        self._scratch = queue._scratch

    def __enter__(self):
        # clear scratch queue
        self._sclear()
        return self

    def __exit__(self, t, v, e):
        # extend callchain with scratch queue
        self._cxtend(self._scratch)
        # clear scratch queue
        self._sclear()

    def __call__(self, args):
        self._sxtend(args)

    def iter(self, args):
        self._sxtend(iter(args))

    def append(self, args):
        self._sappend(args)


class ActiveContextMixin(ResetLocalMixin):

    '''active context mixin'''

    @property
    def _callsync(self):
        return ActiveContext(self)


class ActiveChainlet(ChainletQ, ActiveContext):

    '''active chainlet'''


class ActiveEventlet(EventletQ, ActiveContext):

    '''active eventlet'''


class ActiveLinked(LinkedQ, ActiveContext):

    '''active linked chain'''


class ActiveEventLink(EventLinkQ, ActiveContext):

    '''active linked event'''
