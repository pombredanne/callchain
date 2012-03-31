# -*- coding: utf-8 -*-
'''callchain support'''

from itertools import count
from functools import partial
try:
    from Queue import PriorityQueue, Queue, Empty
except ImportError:
    from queue import PriorityQueue, Queue, Empty  # @UnusedImport
try:
    from functools import total_ordering
except ImportError:
    def total_ordering(cls):
        '''
        class decorator that fills in missing ordering methods

        not available for python versions < 2.7
        '''
        convert = {
            '__lt__': [
                ('__gt__', lambda self, other: not (
                    self < other or self == other)),
                ('__le__', lambda self, other: self < other or self == other),
                ('__ge__', lambda self, other: not self < other),
            ],
            '__le__': [
                ('__ge__',
                lambda self, other: not self <= other or self == other),
                ('__lt__',
                lambda self, other: self <= other and not self == other),
                ('__gt__', lambda self, other: not self <= other),
            ],
            '__gt__': [
                ('__lt__', lambda self, other: not (
                    self > other or self == other)),
                ('__ge__', lambda self, other: self > other or self == other),
                ('__le__', lambda self, other: not self > other),
            ],
            '__ge__': [
                ('__le__', lambda self, other: (
                    not self >= other) or self == other
                ),
                ('__gt__',
                lambda self, other: self >= other and not self == other),
                ('__lt__', lambda self, other: not self >= other)
            ]
        }
        roots = set(dir(cls)) & set(convert)
        if not roots:
            raise ValueError(
                'must define at least one ordering operation: < > <= >='
            )
        # prefer __lt__ to __le__ to __gt__ to __ge__
        root = max(roots)
        for opname, opfunc in convert[root]:
            if opname not in roots:
                opfunc.__name__ = opname
                opfunc.__doc__ = getattr(int, opname).__doc__
                setattr(cls, opname, opfunc)
        return cls

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
