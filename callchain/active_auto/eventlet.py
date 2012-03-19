# -*- coding: utf-8 -*-
'''active auto-balancing eventlets'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.event import EventletQ
from callchain.services.order import KRandom, KOrder
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.services.map import KDelay, KCopy, KRepeat, KMap
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


@appifies(KDelay)
class delayevent(EventletQ, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping eventlet'''


@appifies(KCopy)
class copyevent(EventletQ, AutoQMixin, CopyMixin):

    '''auto-balancing copy eventlet'''


@appifies(KRepeat)
class repeatevent(EventletQ, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat eventlet'''


@appifies(KMap)
class mapevent(EventletQ, AutoQMixin, MapMixin):

    '''auto-balancing mapping eventlet'''


@appifies(KCollect)
class collectevent(EventletQ, AutoQMixin, CollectMixin):

    '''auto-balancing collecting eventlet'''


@appifies(KSet)
class setevent(EventletQ, AutoQMixin, SetMixin):

    '''auto-balancing seting eventlet'''


@appifies(KSlice)
class sliceevent(EventletQ, AutoQMixin, SliceMixin):

    '''auto-balancing slicing eventlet'''


@appifies(KFilter)
class filterevent(EventletQ, AutoQMixin, FilterMixin):

    '''auto-balancing filtering eventlet'''


@appifies(KRandom)
class randomevent(EventletQ, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing eventlet'''


@appifies(KOrder)
class orderevent(EventletQ, AutoQMixin, OrderMixin):

    '''auto-balancing ordering eventlet'''


@appifies(KMath)
class mathevent(EventletQ, AutoQMixin, MathMixin):

    '''auto-balancing mathing eventlet'''


@appifies(KReduce)
class reduceevent(EventletQ, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing eventlet'''


@appifies(KTruth)
class truthevent(EventletQ, AutoQMixin, TruthMixin):

    '''auto-balancing truthing eventlet'''
