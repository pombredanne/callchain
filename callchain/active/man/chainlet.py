# -*- coding: utf-8 -*-
'''active manually balanced chainlets'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter

from callchain.assembly.chainlet import CallChainletQ

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(CallChainletQ, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping chainlets'''


@appifies(KCopy)
class copychain(CallChainletQ, ManQMixin, CopyMixin):

    '''manually balanced copy chainlets'''


@appifies(KRepeat)
class repeatchain(CallChainletQ, ManQMixin, RepeatMixin):

    '''manually balanced repeat chainlets'''


@appifies(KMap)
class mapchain(CallChainletQ, ManQMixin, MapMixin):

    '''manually balanced mapping chainlets'''


@appifies(KCollect)
class collectchain(CallChainletQ, ManQMixin, CollectMixin):

    '''manually balanced collecting chainlets'''


@appifies(KSet)
class setchain(CallChainletQ, ManQMixin, SetMixin):

    '''manually balanced seting chainlets'''


@appifies(KSlice)
class slicechain(CallChainletQ, ManQMixin, SliceMixin):

    '''manually balanced slicing chainlets'''


@appifies(KFilter)
class filterchain(CallChainletQ, ManQMixin, FilterMixin):

    '''manually balanced filtering chainlets'''


@appifies(KRandom)
class randomchain(CallChainletQ, ManQMixin, RandomMixin):

    '''manually balanced randomizing chainlets'''


@appifies(KOrder)
class orderchain(CallChainletQ, ManQMixin, OrderMixin):

    '''manually balanced ordering chainlets'''


@appifies(KMath)
class mathchain(CallChainletQ, ManQMixin, MathMixin):

    '''manually balanced mathing chainlets'''


@appifies(KReduce)
class reducechain(CallChainletQ, ManQMixin, ReduceMixin):

    '''manually balanced reducing chainlets'''


@appifies(KTruth)
class truthchain(CallChainletQ, ManQMixin, TruthMixin):

    '''manually balanced truthing chainlets'''
