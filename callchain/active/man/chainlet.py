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

from callchain.active.mixins import ActiveChainletMixin

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(ActiveChainletMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping chainlets'''


@appifies(KCopy)
class copychain(ActiveChainletMixin, ManQMixin, CopyMixin):

    '''manually balanced copy chainlets'''


@appifies(KRepeat)
class repeatchain(ActiveChainletMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat chainlets'''


@appifies(KMap)
class mapchain(ActiveChainletMixin, ManQMixin, MapMixin):

    '''manually balanced mapping chainlets'''


@appifies(KCollect)
class collectchain(ActiveChainletMixin, ManQMixin, CollectMixin):

    '''manually balanced collecting chainlets'''


@appifies(KSet)
class setchain(ActiveChainletMixin, ManQMixin, SetMixin):

    '''manually balanced seting chainlets'''


@appifies(KSlice)
class slicechain(ActiveChainletMixin, ManQMixin, SliceMixin):

    '''manually balanced slicing chainlets'''


@appifies(KFilter)
class filterchain(ActiveChainletMixin, ManQMixin, FilterMixin):

    '''manually balanced filtering chainlets'''


@appifies(KRandom)
class randomchain(ActiveChainletMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing chainlets'''


@appifies(KOrder)
class orderchain(ActiveChainletMixin, ManQMixin, OrderMixin):

    '''manually balanced ordering chainlets'''


@appifies(KMath)
class mathchain(ActiveChainletMixin, ManQMixin, MathMixin):

    '''manually balanced mathing chainlets'''


@appifies(KReduce)
class reducechain(ActiveChainletMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing chainlets'''


@appifies(KTruth)
class truthchain(ActiveChainletMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing chainlets'''
