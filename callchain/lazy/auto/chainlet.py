# -*- coding: utf-8 -*-
'''lazy auto-balancing chainlets'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter
from callchain.lazy.mixins import LazyChainlet

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


class AutoLazyChainlet(LazyChainlet, AutoQMixin):

    '''lazy auto-balanced chainlet'''


@appifies(KDelay)
class delaychain(AutoLazyChainlet, DelayMixin):

    '''auto-balancing delayed mapping chainlet'''


@appifies(KCopy)
class copychain(AutoLazyChainlet, CopyMixin):

    '''auto-balancing copy chainlet'''


@appifies(KRepeat)
class repeatchain(AutoLazyChainlet, RepeatMixin):

    '''auto-balancing repeat chainlet'''


@appifies(KMap)
class mapchain(AutoLazyChainlet, MapMixin):

    '''auto-balancing mapping chainlet'''


@appifies(KCollect)
class collectchain(AutoLazyChainlet, CollectMixin):

    '''auto-balancing collecting chainlet'''


@appifies(KSet)
class setchain(AutoLazyChainlet, SetMixin):

    '''auto-balancing seting chainlet'''


@appifies(KSlice)
class slicechain(AutoLazyChainlet, SliceMixin):

    '''auto-balancing slicing chainlet'''


@appifies(KFilter)
class filterchain(AutoLazyChainlet, FilterMixin):

    '''auto-balancing filtering chainlet'''


@appifies(KRandom)
class randomchain(AutoLazyChainlet, RandomMixin):

    '''auto-balancing randomizing chainlet'''


@appifies(KOrder)
class orderchain(AutoLazyChainlet, OrderMixin):

    '''auto-balancing ordering chainlet'''


@appifies(KMath)
class mathchain(AutoLazyChainlet, MathMixin):

    '''auto-balancing mathing chainlet'''


@appifies(KReduce)
class reducechain(AutoLazyChainlet, ReduceMixin):

    '''auto-balancing reducing chainlet'''


@appifies(KTruth)
class truthchain(AutoLazyChainlet, TruthMixin):

    '''auto-balancing truthing chainlet'''
