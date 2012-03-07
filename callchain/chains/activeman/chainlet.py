# -*- coding: utf-8 -*-
'''active manually balanced chainlets'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.keys.order import KRandom, KOrder
from callchain.chains.chainlet import ActiveChainletQMixin
from callchain.chains.keys.reduce import KMath, KReduce, KTruth
from callchain.chains.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.chains.keys.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(ActiveChainletQMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping chainlets'''


@appifies(KCopy)
class copychain(ActiveChainletQMixin, ManQMixin, CopyMixin):

    '''manually balanced copy chainlets'''


@appifies(KRepeat)
class repeatchain(ActiveChainletQMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat chainlets'''


@appifies(KMap)
class mapchain(ActiveChainletQMixin, ManQMixin, MapMixin):

    '''manually balanced mapping chainlets'''


@appifies(KCollect)
class collectchain(ActiveChainletQMixin, ManQMixin, CollectMixin):

    '''manually balanced collecting chainlets'''


@appifies(KSet)
class setchain(ActiveChainletQMixin, ManQMixin, SetMixin):

    '''manually balanced seting chainlets'''


@appifies(KSlice)
class slicechain(ActiveChainletQMixin, ManQMixin, SliceMixin):

    '''manually balanced slicing chainlets'''


@appifies(KFilter)
class filterchain(ActiveChainletQMixin, ManQMixin, FilterMixin):

    '''manually balanced filtering chainlets'''


@appifies(KRandom)
class randomchain(ActiveChainletQMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing chainlets'''


@appifies(KOrder)
class orderchain(ActiveChainletQMixin, ManQMixin, OrderMixin):

    '''manually balanced ordering chainlets'''


@appifies(KMath)
class mathchain(ActiveChainletQMixin, ManQMixin, MathMixin):

    '''manually balanced mathing chainlets'''


@appifies(KReduce)
class reducechain(ActiveChainletQMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing chainlets'''


@appifies(KTruth)
class truthchain(ActiveChainletQMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing chainlets'''
