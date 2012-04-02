# -*- coding: utf-8 -*-
'''lazy auto-balanced chainlets'''

from appspace import appifies
from twoq.lazy import AutoQMixin, AutoResultMixin
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


class chainlet(ChainletMixin, BranchMixin, BranchletMixin, AutoQMixin):

    '''chainlet mixin'''


@appifies(KDelay)
class delaychain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    DelayMixin,
):

    '''delayed mapping chainlet'''


@appifies(KRepeat)
class repeatchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    RepeatMixin,
):

    '''repeat chainlet'''


@appifies(KMap)
class mapchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    MapMixin,
):

    '''mapping chainlet'''


@appifies(KCollect)
class collectchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    CollectMixin,
):

    '''collecting chainlet'''


@appifies(KSet)
class setchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    SetMixin,
):

    '''seting chainlet'''


@appifies(KSlice)
class slicechain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    SliceMixin,
):

    '''slicing chainlet'''


@appifies(KFilter)
class filterchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    FilterMixin,
):

    '''filtering chainlet'''


@appifies(KRandom)
class randomchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    RandomMixin,
):

    '''randomizing chainlet'''


@appifies(KOrder)
class orderchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    OrderMixin,
):

    '''ordering chainlet'''


@appifies(KMath)
class mathchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    MathMixin,
):

    '''mathing chainlet'''


@appifies(KReduce)
class reducechain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    ReduceMixin,
):

    '''reducing chainlet'''


@appifies(KCombine)
class combinechain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    CombineMixin,
):

    '''combining chainlet'''


@appifies(KTruth)
class truthchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    TruthMixin,
):

    '''truthing chainlet'''


@appifies(KLinked, KConfig, KCall, KChain, KResult)
class chainlink(BranchMixin, LinkedMixin, ChainMixin, AutoResultMixin):

    '''linked chain'''


@appifies(KLinked, KConfig, KCall, KChain, KResult)
class prioritylink(BranchMixin, LinkedMixin, PriorityMixin, AutoResultMixin):

    '''priority linked chain'''
