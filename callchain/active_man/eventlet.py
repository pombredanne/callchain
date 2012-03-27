# -*- coding: utf-8 -*-
'''active manually balanced eventlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.active.mixins import ManQMixin, ManResultMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.keys.core import KEvent
from callchain.keys.root import KConfig
from callchain.keys.call import KEventCall
from callchain.services.queue import KResult
from callchain.keys.branch import KLinkedKey
from callchain.event import Eventlet, EventLink
from callchain.services.order import KRandom, KOrder
from callchain.services.map import KDelay, KRepeat, KMap
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'repeatevent', 'mapevent',
    'randomevent', 'orderevent',
)


@appifies(KDelay)
class delayevent(Eventlet, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping eventlet'''


@appifies(KRepeat)
class repeatevent(Eventlet, ManQMixin, RepeatMixin):

    '''manually balanced repeat eventlet'''


@appifies(KMap)
class mapevent(Eventlet, ManQMixin, MapMixin):

    '''manually balanced mapping eventlet'''


@appifies(KCollect)
class collectevent(Eventlet, ManQMixin, CollectMixin):

    '''manually balanced collecting eventlet'''


@appifies(KSet)
class setevent(Eventlet, ManQMixin, SetMixin):

    '''manually balanced seting eventlet'''


@appifies(KSlice)
class sliceevent(Eventlet, ManQMixin, SliceMixin):

    '''manually balanced slicing eventlet'''


@appifies(KFilter)
class filterevent(Eventlet, ManQMixin, FilterMixin):

    '''manually balanced filtering eventlet'''


@appifies(KRandom)
class randomevent(Eventlet, ManQMixin, RandomMixin):

    '''manually balanced randomizing eventlet'''


@appifies(KOrder)
class orderevent(Eventlet, ManQMixin, OrderMixin):

    '''manually balanced ordering eventlet'''


@appifies(KMath)
class mathevent(Eventlet, ManQMixin, MathMixin):

    '''manually balanced mathing eventlet'''


@appifies(KReduce)
class reduceevent(Eventlet, ManQMixin, ReduceMixin):

    '''manually balanced reducing eventlet'''


@appifies(KTruth)
class truthevent(Eventlet, ManQMixin, TruthMixin):

    '''manually balanced truthing eventlet'''


@appifies(KLinkedKey, KConfig, KEventCall, KEvent, KResult)
class eventlink(EventLink, ManResultMixin):

    '''manually balanced lite linked event chain'''
