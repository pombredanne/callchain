# -*- coding: utf-8 -*-
'''active manually balanced eventlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.active.mixins import ManQMixin, ManResultMixin
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
from callchain.services.filter import KCollect, KSet, KSlice, KFilter
from callchain.branch import (
    ChainletMixin, EventBranchMixin, BranchletMixin, LinkedMixin)

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'repeatevent', 'mapevent',
    'randomevent', 'orderevent',
)


@appifies(KDelay)
class delayevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    DelayMixin,
):

    '''manually balanced delayed mapping eventlet'''


@appifies(KRepeat)
class repeatevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    RepeatMixin,
):

    '''manually balanced repeat eventlet'''


@appifies(KMap)
class mapevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    MapMixin,
):

    '''manually balanced mapping eventlet'''


@appifies(KCollect)
class collectevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    CollectMixin,
):

    '''manually balanced collecting eventlet'''


@appifies(KSet)
class setevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    SetMixin,
):

    '''manually balanced seting eventlet'''


@appifies(KSlice)
class sliceevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    SliceMixin,
):

    '''manually balanced slicing eventlet'''


@appifies(KFilter)
class filterevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    FilterMixin,
):

    '''manually balanced filtering eventlet'''


@appifies(KRandom)
class randomevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    RandomMixin,
):

    '''manually balanced randomizing eventlet'''


@appifies(KOrder)
class orderevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    OrderMixin,
):

    '''manually balanced ordering eventlet'''


@appifies(KMath)
class mathevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    MathMixin,
):

    '''manually balanced mathing eventlet'''


@appifies(KReduce)
class reduceevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    ReduceMixin,
):

    '''manually balanced reducing eventlet'''


@appifies(KTruth)
class truthevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    ManQMixin,
    TruthMixin,
):

    '''manually balanced truthing eventlet'''


@appifies(KLinked, KConfig, KEventCall, KEvent, KResult)
class eventlink(EventBranchMixin, LinkedMixin, EventMixin, ManResultMixin):

    '''manually balanced lite linked event chain'''
