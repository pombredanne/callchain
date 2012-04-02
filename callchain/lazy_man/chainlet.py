# -*- coding: utf-8 -*-
'''lazy manually balanced chainlets'''

from appspace import appifies
from twoq.lazy import ManQMixin, ManResultMixin
from twoq.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.ordering import RandomMixin, OrderMixin, CombineMixin
from twoq.filtering import FilterMixin, CollectMixin, SetMixin, SliceMixin

from callchain.services import KResult
from callchain.call import ChainMixin, PriorityMixin
from callchain.services.map import KDelay, KRepeat, KMap
from callchain.keys import KCall, KChain, KConfig, KLinked
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.chain import (
    BranchMixin, BranchletMixin, ChainletMixin, LinkedMixin)
from callchain.services.order import KRandom, KOrder, KCombine
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'repeatchain', 'mapchain',
    'randomchain', 'orderchain', 'chainlet', 'combinechain',
)


class chainlet(ChainletMixin, BranchMixin, BranchletMixin, ManQMixin):

    '''chainlet mixin'''


@appifies(KDelay)
class delaychain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    DelayMixin,
):

    '''delayed mapping chainlet'''


@appifies(KRepeat)
class repeatchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    RepeatMixin,
):

    '''repeat chainlet'''


@appifies(KMap)
class mapchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    MapMixin,
):

    '''mapping chainlet'''


@appifies(KCollect)
class collectchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    CollectMixin,
):

    '''collecting chainlet'''


@appifies(KSet)
class setchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    SetMixin,
):

    '''seting chainlet'''


@appifies(KSlice)
class slicechain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    SliceMixin,
):

    '''slicing chainlet'''


@appifies(KFilter)
class filterchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    FilterMixin,
):

    '''filtering chainlet'''


@appifies(KRandom)
class randomchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    RandomMixin,
):

    '''randomizing chainlet'''


@appifies(KOrder)
class orderchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    OrderMixin,
):

    '''ordering chainlet'''


@appifies(KMath)
class mathchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    MathMixin,
):

    '''mathing chainlet'''


@appifies(KReduce)
class reducechain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    ReduceMixin,
):

    '''reducing chainlet'''


@appifies(KCombine)
class combinechain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    CombineMixin,
):

    '''combining chainlet'''


@appifies(KTruth)
class truthchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    TruthMixin,
):

    '''truthing chainlet'''


@appifies(KLinked, KConfig, KCall, KChain, KResult)
class chainlink(BranchMixin, LinkedMixin, ChainMixin, ManResultMixin):

    '''linked chain'''


@appifies(KLinked, KConfig, KCall, KChain, KResult)
class prioritylink(BranchMixin, LinkedMixin, PriorityMixin, ManResultMixin):

    '''priority linked chain'''
