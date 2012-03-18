# -*- coding: utf-8 -*-
'''active manually balanced chainlets'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chainlet import ActiveChainlet
from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(ActiveChainlet, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping chainlet'''


@appifies(KCopy)
class copychain(ActiveChainlet, ManQMixin, CopyMixin):

    '''manually balanced copy chainlet'''


@appifies(KRepeat)
class repeatchain(ActiveChainlet, ManQMixin, RepeatMixin):

    '''manually balanced repeat chainlet'''


@appifies(KMap)
class mapchain(ActiveChainlet, ManQMixin, MapMixin):

    '''manually balanced mapping chainlet'''


@appifies(KCollect)
class collectchain(ActiveChainlet, ManQMixin, CollectMixin):

    '''manually balanced collecting chainlet'''


@appifies(KSet)
class setchain(ActiveChainlet, ManQMixin, SetMixin):

    '''manually balanced seting chainlet'''


@appifies(KSlice)
class slicechain(ActiveChainlet, ManQMixin, SliceMixin):

    '''manually balanced slicing chainlet'''


@appifies(KFilter)
class filterchain(ActiveChainlet, ManQMixin, FilterMixin):

    '''manually balanced filtering chainlet'''


@appifies(KRandom)
class randomchain(ActiveChainlet, ManQMixin, RandomMixin):

    '''manually balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(ActiveChainlet, ManQMixin, OrderMixin):

    '''manually balanced ordering chainlet'''


@appifies(KMath)
class mathchain(ActiveChainlet, ManQMixin, MathMixin):

    '''manually balanced mathing chainlet'''


@appifies(KReduce)
class reducechain(ActiveChainlet, ManQMixin, ReduceMixin):

    '''manually balanced reducing chainlet'''


@appifies(KTruth)
class truthchain(ActiveChainlet, ManQMixin, TruthMixin):

    '''manually balanced truthing chainlet'''
