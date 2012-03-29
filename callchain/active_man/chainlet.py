# -*- coding: utf-8 -*-
'''active manually balanced chainlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.active.mixins import ManQMixin, ManResultMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.call import ChainMixin
from callchain.keys.call import KCall
from callchain.keys.core import KChain
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

    '''manually balanced delayed mapping chainlet'''


@appifies(KRepeat)
class repeatchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    RepeatMixin,
):

    '''manually balanced repeat chainlet'''


@appifies(KMap)
class mapchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    MapMixin,
):

    '''manually balanced mapping chainlet'''


@appifies(KCollect)
class collectchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    CollectMixin,
):

    '''manually balanced collecting chainlet'''


@appifies(KSet)
class setchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    SetMixin,
):

    '''manually balanced setting chainlet'''


@appifies(KSlice)
class slicechain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    SliceMixin,
):

    '''manually balanced slicing chainlet'''


@appifies(KFilter)
class filterchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    FilterMixin,
):

    '''manually balanced filtering chainlet'''


@appifies(KRandom)
class randomchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    RandomMixin,
):

    '''manually balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    OrderMixin,
):

    '''manually balanced ordering chainlet'''


@appifies(KMath)
class mathchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    MathMixin,
):

    '''manually balanced mathing chainlet'''


@appifies(KReduce)
class reducechain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    ReduceMixin,
):

    '''manually balanced reducing chainlet'''


@appifies(KTruth)
class truthchain(
    ChainletMixin,
    BranchMixin,
    BranchletMixin,
    ManQMixin,
    TruthMixin,
):

    '''manually balanced truthing chainlet'''


@appifies(KLinked, KConfig, KCall, KChain, KResult)
class chainlink(BranchMixin, LinkedMixin, ChainMixin, ManResultMixin):

    '''manually balanced linked chain'''
