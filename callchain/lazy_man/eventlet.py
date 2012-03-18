# -*- coding: utf-8 -*-
'''lazy manually balanced eventlets'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chainlet import LazyEventlet
from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


@appifies(KDelay)
class delayevent(LazyEventlet, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping eventlet'''


@appifies(KCopy)
class copyevent(LazyEventlet, ManQMixin, CopyMixin):

    '''manually balanced copy eventlet'''


@appifies(KRepeat)
class repeatevent(LazyEventlet, ManQMixin, RepeatMixin):

    '''manually balanced repeat eventlet'''


@appifies(KMap)
class mapevent(LazyEventlet, ManQMixin, MapMixin):

    '''manually balanced mapping eventlet'''


@appifies(KCollect)
class collectevent(LazyEventlet, ManQMixin, CollectMixin):

    '''manually balanced collecting eventlet'''


@appifies(KSet)
class setevent(LazyEventlet, ManQMixin, SetMixin):

    '''manually balanced seting eventlet'''


@appifies(KSlice)
class sliceevent(LazyEventlet, ManQMixin, SliceMixin):

    '''manually balanced slicing eventlet'''


@appifies(KFilter)
class filterevent(LazyEventlet, ManQMixin, FilterMixin):

    '''manually balanced filtering eventlet'''


@appifies(KRandom)
class randomevent(LazyEventlet, ManQMixin, RandomMixin):

    '''manually balanced randomizing eventlet'''


@appifies(KOrder)
class orderevent(LazyEventlet, ManQMixin, OrderMixin):

    '''manually balanced ordering eventlet'''


@appifies(KMath)
class mathevent(LazyEventlet, ManQMixin, MathMixin):

    '''manually balanced mathing eventlet'''


@appifies(KReduce)
class reduceevent(LazyEventlet, ManQMixin, ReduceMixin):

    '''manually balanced reducing eventlet'''


@appifies(KTruth)
class truthevent(LazyEventlet, ManQMixin, TruthMixin):

    '''manually balanced truthing eventlet'''
