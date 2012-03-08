# -*- coding: utf-8 -*-
'''lazy manually balanced chainlet event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter

from callchain.lazy.mixins import LazyELetMixin

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


@appifies(KDelay)
class delayevent(LazyELetMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping chainlet event chain'''


@appifies(KCopy)
class copyevent(LazyELetMixin, ManQMixin, CopyMixin):

    '''manually balanced copy chainlet event chain'''


@appifies(KRepeat)
class repeatevent(LazyELetMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat chainlet event chain'''


@appifies(KMap)
class mapevent(LazyELetMixin, ManQMixin, MapMixin):

    '''manually balanced mapping chainlet event chain'''


@appifies(KCollect)
class collectevent(LazyELetMixin, ManQMixin, CollectMixin):

    '''manually balanced collecting chainlet event chain'''


@appifies(KSet)
class setevent(LazyELetMixin, ManQMixin, SetMixin):

    '''manually balanced seting chainlet event chain'''


@appifies(KSlice)
class sliceevent(LazyELetMixin, ManQMixin, SliceMixin):

    '''manually balanced slicing chainlet event chain'''


@appifies(KFilter)
class filterevent(LazyELetMixin, ManQMixin, FilterMixin):

    '''manually balanced filtering chainlet event chain'''


@appifies(KRandom)
class randomevent(LazyELetMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing chainlet event chain'''


@appifies(KOrder)
class orderevent(LazyELetMixin, ManQMixin, OrderMixin):

    '''manually balanced ordering chainlet event chain'''


@appifies(KMath)
class mathevent(LazyELetMixin, ManQMixin, MathMixin):

    '''manually balanced mathing chainlet event chain'''


@appifies(KReduce)
class reduceevent(LazyELetMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing chainlet event chain'''


@appifies(KTruth)
class truthevent(LazyELetMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing chainlet event chain'''
