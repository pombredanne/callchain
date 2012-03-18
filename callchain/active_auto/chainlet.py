# -*- coding: utf-8 -*-
'''active auto-balancing chainlets'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter

from callchain.chainlet import ActiveChainlet

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


class AutoActiveChainlet(ActiveChainlet, AutoQMixin):

    '''active auto-balancing chainlet'''


@appifies(KDelay)
class delaychain(AutoActiveChainlet, DelayMixin):

    '''auto-balancing delayed mapping chainlet'''


@appifies(KCopy)
class copychain(AutoActiveChainlet, CopyMixin):

    '''auto-balancing copy chainlet'''


@appifies(KRepeat)
class repeatchain(AutoActiveChainlet, RepeatMixin):

    '''auto-balancing repeat chainlet'''


@appifies(KMap)
class mapchain(AutoActiveChainlet, MapMixin):

    '''auto-balancing mapping chainlet'''


@appifies(KCollect)
class collectchain(AutoActiveChainlet, CollectMixin):

    '''auto-balancing collecting chainlet'''


@appifies(KSet)
class setchain(AutoActiveChainlet, SetMixin):

    '''auto-balancing seting chainlet'''


@appifies(KSlice)
class slicechain(AutoActiveChainlet, SliceMixin):

    '''auto-balancing slicing chainlet'''


@appifies(KFilter)
class filterchain(AutoActiveChainlet, FilterMixin):

    '''auto-balancing filtering chainlet'''


@appifies(KRandom)
class randomchain(AutoActiveChainlet, RandomMixin):

    '''auto-balancing randomizing chainlet'''


@appifies(KOrder)
class orderchain(AutoActiveChainlet, OrderMixin):

    '''auto-balancing ordering chainlet'''


@appifies(KMath)
class mathchain(AutoActiveChainlet, MathMixin):

    '''auto-balancing mathing chainlet'''


@appifies(KReduce)
class reducechain(AutoActiveChainlet, ReduceMixin):

    '''auto-balancing reducing chainlet'''


@appifies(KTruth)
class truthchain(AutoActiveChainlet, TruthMixin):

    '''auto-balancing truthing chainlet'''
