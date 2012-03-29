# -*- coding: utf-8 -*-
'''active auto-balancing eventlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.active.mixins import AutoQMixin, AutoResultMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.call import EventMixin
from callchain.keys.core import KEvent
from callchain.keys.root import KConfig
from callchain.keys.branch import KLinked
from callchain.keys.call import KEventCall
from callchain.services.queue import KResult
from callchain.services.order import KRandom, KOrder
from callchain.services.map import KDelay, KRepeat, KMap
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.branch import (
    ChainletMixin, EventBranchMixin, BranchletMixin, LinkedMixin)
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'repeatevent', 'mapevent',
    'randomevent', 'orderevent', 'eventlet'
)


class eventlet(ChainletMixin, EventBranchMixin, BranchletMixin, AutoQMixin):

    '''eventlet mixin'''


@appifies(KDelay)
class delayevent(eventlet, DelayMixin):

    '''delayed mapping eventlet'''


@appifies(KRepeat)
class repeatevent(eventlet, RepeatMixin):

    '''repeat eventlet'''


@appifies(KMap)
class mapevent(eventlet, MapMixin):

    '''mapping eventlet'''


@appifies(KCollect)
class collectevent(eventlet, CollectMixin):

    '''collecting eventlet'''


@appifies(KSet)
class setevent(eventlet, SetMixin):

    '''seting eventlet'''


@appifies(KSlice)
class sliceevent(eventlet, SliceMixin):

    '''slicing eventlet'''


@appifies(KFilter)
class filterevent(eventlet, FilterMixin):

    '''filtering eventlet'''


@appifies(KRandom)
class randomevent(eventlet, RandomMixin):

    '''randomizing eventlet'''


@appifies(KOrder)
class orderevent(eventlet, OrderMixin):

    '''ordering eventlet'''


@appifies(KMath)
class mathevent(eventlet, MathMixin):

    '''mathing eventlet'''


@appifies(KReduce)
class reduceevent(eventlet, ReduceMixin):

    '''reducing eventlet'''


@appifies(KTruth)
class truthevent(eventlet, TruthMixin):

    '''truthing eventlet'''


@appifies(KLinked, KConfig, KEventCall, KEvent, KResult)
class eventlink(EventBranchMixin, LinkedMixin, EventMixin, AutoResultMixin):

    '''lite linked event chain'''
