# -*- coding: utf-8 -*-
'''lazy auto-balancing eventlets'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.queuing import FingerMixin, ResultMixin, CallableMixin

from callchain.event import EventletQ
from callchain.services.order import KRandom, KOrder
from callchain.services.map import KDelay, KRepeat, KMap
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.services.queue import KCallable, KResults, KFinger
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'repeatevent', 'mapevent',
    'randomevent', 'orderevent', 'fingerevent', 'resultevent', 'callablevent',
)


@appifies(KDelay)
class delayevent(EventletQ, AutoMixin, DelayMixin):

    '''auto-balancing delayed mapping eventlet'''


@appifies(KFinger)
class fingerevent(EventletQ, AutoMixin, FingerMixin):

    '''auto-balancing fingering eventlet'''


@appifies(KResults)
class resultevent(EventletQ, AutoMixin, ResultMixin):

    '''auto-balancing results eventlet'''


@appifies(KCallable)
class callablevent(EventletQ, AutoMixin, CallableMixin):

    '''auto-balancing callable eventlet'''


@appifies(KRepeat)
class repeatevent(EventletQ, AutoMixin, RepeatMixin):

    '''auto-balancing repeat eventlet'''


@appifies(KMap)
class mapevent(EventletQ, AutoMixin, MapMixin):

    '''auto-balancing mapping eventlet'''


@appifies(KCollect)
class collectevent(EventletQ, AutoMixin, CollectMixin):

    '''auto-balancing collecting eventlet'''


@appifies(KSet)
class setevent(EventletQ, AutoMixin, SetMixin):

    '''auto-balancing seting eventlet'''


@appifies(KSlice)
class sliceevent(EventletQ, AutoMixin, SliceMixin):

    '''auto-balancing slicing eventlet'''


@appifies(KFilter)
class filterevent(EventletQ, AutoMixin, FilterMixin):

    '''auto-balancing filtering eventlet'''


@appifies(KRandom)
class randomevent(EventletQ, AutoMixin, RandomMixin):

    '''auto-balancing randomizing eventlet'''


@appifies(KOrder)
class orderevent(EventletQ, AutoMixin, OrderMixin):

    '''auto-balancing ordering eventlet'''


@appifies(KMath)
class mathevent(EventletQ, AutoMixin, MathMixin):

    '''auto-balancing mathing eventlet'''


@appifies(KReduce)
class reduceevent(EventletQ, AutoMixin, ReduceMixin):

    '''auto-balancing reducing eventlet'''


@appifies(KTruth)
class truthevent(EventletQ, AutoMixin, TruthMixin):

    '''auto-balancing truthing eventlet'''
