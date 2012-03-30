# -*- coding: utf-8 -*-
'''lazy lazy balanced chainlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.lazy.mixins import AutoQMixin, AutoResultMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.keys.call import KCall
from callchain.keys.core import KChain
from callchain.keys.root import KConfig
from callchain.keys.branch import KLinked
from callchain.services.queue import KResult
from callchain.call import ChainMixin, PriorityMixin
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

    '''lazy balanced delayed mapping chainlet'''


@appifies(KRepeat)
class repeatchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    RepeatMixin,
):

    '''lazy balanced repeat chainlet'''


@appifies(KMap)
class mapchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    MapMixin,
):

    '''lazy balanced mapping chainlet'''


@appifies(KCollect)
class collectchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    CollectMixin,
):

    '''lazy balanced collecting chainlet'''


@appifies(KSet)
class setchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    SetMixin,
):

    '''lazy balanced seting chainlet'''


@appifies(KSlice)
class slicechain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    SliceMixin,
):

    '''lazy balanced slicing chainlet'''


@appifies(KFilter)
class filterchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    FilterMixin,
):

    '''lazy balanced filtering chainlet'''


@appifies(KRandom)
class randomchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    RandomMixin,
):

    '''lazy balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    OrderMixin,
):

    '''lazy balanced ordering chainlet'''


@appifies(KMath)
class mathchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    MathMixin,
):

    '''lazy balanced mathing chainlet'''


@appifies(KReduce)
class reducechain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    ReduceMixin,
):

    '''lazy balanced reducing chainlet'''


@appifies(KTruth)
class truthchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    AutoQMixin,
    TruthMixin,
):

    '''lazy balanced truthing chainlet'''


@appifies(KLinked, KConfig, KCall, KChain, KResult)
class chainlink(BranchMixin, LinkedMixin, ChainMixin, AutoResultMixin):

    '''lazy balanced linked chain'''


@appifies(KLinked, KConfig, KCall, KChain, KResult)
class prilink(BranchMixin, LinkedMixin, PriorityMixin, AutoResultMixin):

    '''lazy balanced priority linked chain'''
