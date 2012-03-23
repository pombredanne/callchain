# -*- coding: utf-8 -*-
'''active manually balanced eventlets'''

from appspace.keys import appifies
from twoq.active.mixins import ManMixin
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
class delayevent(EventletQ, ManMixin, DelayMixin):

    '''manually balanced delayed mapping eventlet'''


@appifies(KFinger)
class fingerevent(EventletQ, ManMixin, FingerMixin):

    '''manually balanced fingering eventlet'''


@appifies(KResults)
class resultevent(EventletQ, ManMixin, ResultMixin):

    '''manually balanced results eventlet'''


@appifies(KCallable)
class callablevent(EventletQ, ManMixin, CallableMixin):

    '''manually balanced callable eventlet'''


@appifies(KRepeat)
class repeatevent(EventletQ, ManMixin, RepeatMixin):

    '''manually balanced repeat eventlet'''


@appifies(KMap)
class mapevent(EventletQ, ManMixin, MapMixin):

    '''manually balanced mapping eventlet'''


@appifies(KCollect)
class collectevent(EventletQ, ManMixin, CollectMixin):

    '''manually balanced collecting eventlet'''


@appifies(KSet)
class setevent(EventletQ, ManMixin, SetMixin):

    '''manually balanced seting eventlet'''


@appifies(KSlice)
class sliceevent(EventletQ, ManMixin, SliceMixin):

    '''manually balanced slicing eventlet'''


@appifies(KFilter)
class filterevent(EventletQ, ManMixin, FilterMixin):

    '''manually balanced filtering eventlet'''


@appifies(KRandom)
class randomevent(EventletQ, ManMixin, RandomMixin):

    '''manually balanced randomizing eventlet'''


@appifies(KOrder)
class orderevent(EventletQ, ManMixin, OrderMixin):

    '''manually balanced ordering eventlet'''


@appifies(KMath)
class mathevent(EventletQ, ManMixin, MathMixin):

    '''manually balanced mathing eventlet'''


@appifies(KReduce)
class reduceevent(EventletQ, ManMixin, ReduceMixin):

    '''manually balanced reducing eventlet'''


@appifies(KTruth)
class truthevent(EventletQ, ManMixin, TruthMixin):

    '''manually balanced truthing eventlet'''
