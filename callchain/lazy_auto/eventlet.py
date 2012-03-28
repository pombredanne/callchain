# -*- coding: utf-8 -*-
'''lazy auto-balancing eventlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.lazy.mixins import AutoQMixin, AutoResultMixin
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
class delayevent(Eventlet, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping eventlet'''


@appifies(KRepeat)
class repeatevent(Eventlet, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat eventlet'''


@appifies(KMap)
class mapevent(Eventlet, AutoQMixin, MapMixin):

    '''auto-balancing mapping eventlet'''


@appifies(KCollect)
class collectevent(Eventlet, AutoQMixin, CollectMixin):

    '''auto-balancing collecting eventlet'''


@appifies(KSet)
class setevent(Eventlet, AutoQMixin, SetMixin):

    '''auto-balancing seting eventlet'''


@appifies(KSlice)
class sliceevent(Eventlet, AutoQMixin, SliceMixin):

    '''auto-balancing slicing eventlet'''


@appifies(KFilter)
class filterevent(Eventlet, AutoQMixin, FilterMixin):

    '''auto-balancing filtering eventlet'''


@appifies(KRandom)
class randomevent(Eventlet, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing eventlet'''


@appifies(KOrder)
class orderevent(Eventlet, AutoQMixin, OrderMixin):

    '''auto-balancing ordering eventlet'''


@appifies(KMath)
class mathevent(Eventlet, AutoQMixin, MathMixin):

    '''auto-balancing mathing eventlet'''


@appifies(KReduce)
class reduceevent(Eventlet, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing eventlet'''


@appifies(KTruth)
class truthevent(Eventlet, AutoQMixin, TruthMixin):

    '''auto-balancing truthing eventlet'''


@appifies(KLinkedKey, KConfig, KEventCall, KEvent, KResult)
class eventlink(EventLink, AutoResultMixin):

    '''auto-balancing lite linked event chain'''
