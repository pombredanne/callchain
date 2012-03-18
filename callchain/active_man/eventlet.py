# -*- coding: utf-8 -*-
'''active manually balanced eventlets'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chainlet import ActiveEventlet
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
class delayevent(ActiveEventlet, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping eventlet'''


@appifies(KCopy)
class copyevent(ActiveEventlet, ManQMixin, CopyMixin):

    '''manually balanced copy eventlet'''


@appifies(KRepeat)
class repeatevent(ActiveEventlet, ManQMixin, RepeatMixin):

    '''manually balanced repeat eventlet'''


@appifies(KMap)
class mapevent(ActiveEventlet, ManQMixin, MapMixin):

    '''manually balanced mapping eventlet'''


@appifies(KCollect)
class collectevent(ActiveEventlet, ManQMixin, CollectMixin):

    '''manually balanced collecting eventlet'''


@appifies(KSet)
class setevent(ActiveEventlet, ManQMixin, SetMixin):

    '''manually balanced seting eventlet'''


@appifies(KSlice)
class sliceevent(ActiveEventlet, ManQMixin, SliceMixin):

    '''manually balanced slicing eventlet'''


@appifies(KFilter)
class filterevent(ActiveEventlet, ManQMixin, FilterMixin):

    '''manually balanced filtering eventlet'''


@appifies(KRandom)
class randomevent(ActiveEventlet, ManQMixin, RandomMixin):

    '''manually balanced randomizing eventlet'''


@appifies(KOrder)
class orderevent(ActiveEventlet, ManQMixin, OrderMixin):

    '''manually balanced ordering eventlet'''


@appifies(KMath)
class mathevent(ActiveEventlet, ManQMixin, MathMixin):

    '''manually balanced mathing eventlet'''


@appifies(KReduce)
class reduceevent(ActiveEventlet, ManQMixin, ReduceMixin):

    '''manually balanced reducing eventlet'''


@appifies(KTruth)
class truthevent(ActiveEventlet, ManQMixin, TruthMixin):

    '''manually balanced truthing eventlet'''
