# -*- coding: utf-8 -*-
'''active auto-balancing eventlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.active.mixins import AutoQMixin, AutoResultMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.core import EventMixin
from callchain.keys.core import KEvent
from callchain.keys.root import KConfig
from callchain.keys.branch import KLinked
from callchain.call import EventCallMixin
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
    EventMixin,
    AutoQMixin,
    DelayMixin,
):

    '''auto-balancing delayed mapping eventlet'''


@appifies(KRepeat)
class repeatevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    EventMixin,
    AutoQMixin,
    RepeatMixin,
):

    '''auto-balancing repeat eventlet'''


@appifies(KMap)
class mapevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    EventMixin,
    AutoQMixin,
    MapMixin,
):

    '''auto-balancing mapping eventlet'''


@appifies(KCollect)
class collectevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    EventMixin,
    AutoQMixin,
    CollectMixin,
):

    '''auto-balancing collecting eventlet'''


@appifies(KSet)
class setevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin, EventMixin,
    AutoQMixin,
    SetMixin,
):

    '''auto-balancing seting eventlet'''


@appifies(KSlice)
class sliceevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    EventMixin,
    AutoQMixin,
    SliceMixin,
):

    '''auto-balancing slicing eventlet'''


@appifies(KFilter)
class filterevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    EventMixin,
    AutoQMixin,
    FilterMixin,
):

    '''auto-balancing filtering eventlet'''


@appifies(KRandom)
class randomevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    EventMixin,
    AutoQMixin,
    RandomMixin,
):

    '''auto-balancing randomizing eventlet'''


@appifies(KOrder)
class orderevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    EventMixin,
    AutoQMixin,
    OrderMixin,
):

    '''auto-balancing ordering eventlet'''


@appifies(KMath)
class mathevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    EventMixin,
    AutoQMixin,
    MathMixin,
):

    '''auto-balancing mathing eventlet'''


@appifies(KReduce)
class reduceevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    EventMixin,
    AutoQMixin,
    ReduceMixin,
):

    '''auto-balancing reducing eventlet'''


@appifies(KTruth)
class truthevent(
    ChainletMixin,
    EventBranchMixin,
    BranchletMixin,
    EventMixin,
    AutoQMixin,
    TruthMixin,
):

    '''auto-balancing truthing eventlet'''


@appifies(KLinked, KConfig, KEventCall, KEvent, KResult)
class eventlink(
    EventCallMixin, EventBranchMixin, LinkedMixin, EventMixin, AutoResultMixin,
):

    '''auto-balancing lite linked event chain'''
