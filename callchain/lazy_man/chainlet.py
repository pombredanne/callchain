# -*- coding: utf-8 -*-
'''lazy manually balanced chainlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.lazy.mixins import ManQMixin, ManResultMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
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
    ManQMixin,
    DelayMixin,
):

    '''manually balanced delayed mapping chainlet'''


@appifies(KRepeat)
class repeatchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    RepeatMixin,
):

    '''manually balanced repeat chainlet'''


@appifies(KMap)
class mapchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    MapMixin,
):

    '''manually balanced mapping chainlet'''


@appifies(KCollect)
class collectchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    CollectMixin,
):

    '''manually balanced collecting chainlet'''


@appifies(KSet)
class setchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    SetMixin,
):

    '''manually balanced setting chainlet'''


@appifies(KSlice)
class slicechain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    SliceMixin,
):

    '''manually balanced slicing chainlet'''


@appifies(KFilter)
class filterchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    FilterMixin,
):

    '''manually balanced filtering chainlet'''


@appifies(KRandom)
class randomchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    RandomMixin,
):

    '''manually balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    OrderMixin,
):

    '''manually balanced ordering chainlet'''


@appifies(KMath)
class mathchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    MathMixin,
):

    '''manually balanced mathing chainlet'''


@appifies(KReduce)
class reducechain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    ReduceMixin,
):

    '''manually balanced reducing chainlet'''


@appifies(KTruth)
class truthchain(
    ChainletMixin,
    BranchletMixin,
    BranchMixin,
    ChainMixin,
    ManQMixin,
    TruthMixin,
):

    '''manually balanced truthing chainlet'''


@appifies(KLinked, KConfig, KCall, KChain, KResult)
class chainlink(
    CallMixin, BranchMixin, LinkedMixin, ChainMixin, ManResultMixin,
):

    '''manually balanced linked chain'''
