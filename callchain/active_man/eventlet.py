# -*- coding: utf-8 -*-
'''active manually balanced eventlets'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chainlet import ActiveEventletQ
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
class delayevent(ActiveEventletQ, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping eventlet'''


@appifies(KCopy)
class copyevent(ActiveEventletQ, ManQMixin, CopyMixin):

    '''manually balanced copy eventlet'''


@appifies(KRepeat)
class repeatevent(ActiveEventletQ, ManQMixin, RepeatMixin):

    '''manually balanced repeat eventlet'''


@appifies(KMap)
class mapevent(ActiveEventletQ, ManQMixin, MapMixin):

    '''manually balanced mapping eventlet'''


@appifies(KCollect)
class collectevent(ActiveEventletQ, ManQMixin, CollectMixin):

    '''manually balanced collecting eventlet'''


@appifies(KSet)
class setevent(ActiveEventletQ, ManQMixin, SetMixin):

    '''manually balanced seting eventlet'''


@appifies(KSlice)
class sliceevent(ActiveEventletQ, ManQMixin, SliceMixin):

    '''manually balanced slicing eventlet'''


@appifies(KFilter)
class filterevent(ActiveEventletQ, ManQMixin, FilterMixin):

    '''manually balanced filtering eventlet'''


@appifies(KRandom)
class randomevent(ActiveEventletQ, ManQMixin, RandomMixin):

    '''manually balanced randomizing eventlet'''


@appifies(KOrder)
class orderevent(ActiveEventletQ, ManQMixin, OrderMixin):

    '''manually balanced ordering eventlet'''


@appifies(KMath)
class mathevent(ActiveEventletQ, ManQMixin, MathMixin):

    '''manually balanced mathing eventlet'''


@appifies(KReduce)
class reduceevent(ActiveEventletQ, ManQMixin, ReduceMixin):

    '''manually balanced reducing eventlet'''


@appifies(KTruth)
class truthevent(ActiveEventletQ, ManQMixin, TruthMixin):

    '''manually balanced truthing eventlet'''
