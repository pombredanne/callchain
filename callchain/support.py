# -*- coding: utf-8 -*-
'''callchain support'''

from itertools import count
from functools import partial, total_ordering
try:
    from Queue import PriorityQueue, Queue, Empty
except ImportError:
    from queue import PriorityQueue, Queue, Empty  # @UnusedImport

from stuf.utils import lazy_set, setter


@total_ordering
class cury(object):

    __slots__ = ('_call', 'count')

    counter = count()

    def __init__(self, call, *args, **kw):
        self._call = partial(call, *args, **kw)
        priority = kw.pop('priority', None)
        self.count = next(self.counter) if priority is None else priority

    def __call__(self):
        return self._call()

    def __lt__(self, other):
        return self.count < other


class lock_set(lazy_set):

    '''lazily assign attributes with a custom setter'''

    def __get__(self, this, that):
        if this is None:
            return self
        # check if settings are locked
        if this._locked:
            return setter(this, self.name, self.method(this))
        return self.method(this)
