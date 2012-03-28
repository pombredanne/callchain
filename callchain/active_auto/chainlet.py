# -*- coding: utf-8 -*-
'''active auto-balancing chainlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.active.mixins import AutoQMixin, AutoResultMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.call import CallMixin
from callchain.keys.call import KCall
from callchain.keys.core import KChain
from callchain.core import ChainMixin
from callchain.keys.root import KConfig
from callchain.keys.branch import KLinked
from callchain.services.queue import KResult
from callchain.services.order import KRandom, KOrder
from callchain.services.map import KDelay, KRepeat, KMap
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.branch import (
    BranchMixin, BranchletMixin, ChainletMixin, LinkedMixin)
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'repeatchain', 'mapchain',
    'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    DelayMixin,
):

    '''auto-balancing delayed mapping chainlet'''


@appifies(KRepeat)
class repeatchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    RepeatMixin,
):

    '''auto-balancing repeat chainlet'''


@appifies(KMap)
class mapchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    MapMixin,
):

    '''auto-balancing mapping chainlet'''


@appifies(KCollect)
class collectchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    CollectMixin,
):

    '''auto-balancing collecting chainlet'''


@appifies(KSet)
class setchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    SetMixin,
):

    '''auto-balancing seting chainlet'''


@appifies(KSlice)
class slicechain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    SliceMixin,
):

    '''auto-balancing slicing chainlet'''


@appifies(KFilter)
class filterchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    FilterMixin,
):

    '''auto-balancing filtering chainlet'''


@appifies(KRandom)
class randomchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    RandomMixin,
):

    '''auto-balancing randomizing chainlet'''


@appifies(KOrder)
class orderchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    OrderMixin,
):

    '''auto-balancing ordering chainlet'''


@appifies(KMath)
class mathchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    MathMixin,
):

    '''auto-balancing mathing chainlet'''


@appifies(KReduce)
class reducechain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    ReduceMixin,
):

    '''auto-balancing reducing chainlet'''


@appifies(KTruth)
class truthchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    AutoQMixin,
    TruthMixin,
):

    '''auto-balancing truthing chainlet'''


@appifies(KLinked, KConfig, KCall, KChain, KResult)
class chainlink(
    CallMixin, BranchMixin, LinkedMixin, ChainMixin, AutoResultMixin,
):

    '''auto-balancing linked chain'''
