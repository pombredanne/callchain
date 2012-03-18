# -*- coding: utf-8 -*-
'''lazy auto-balancing chainlets'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chainlet import LazyChainlet
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
class delaychain(LazyChainlet, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping chainlet'''


@appifies(KCopy)
class copychain(LazyChainlet, AutoQMixin, CopyMixin):

    '''auto-balancing copy chainlet'''


@appifies(KRepeat)
class repeatchain(LazyChainlet, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat chainlet'''


@appifies(KMap)
class mapchain(LazyChainlet, AutoQMixin, MapMixin):

    '''auto-balancing mapping chainlet'''


@appifies(KCollect)
class collectchain(LazyChainlet, AutoQMixin, CollectMixin):

    '''auto-balancing collecting chainlet'''


@appifies(KSet)
class setchain(LazyChainlet, AutoQMixin, SetMixin):

    '''auto-balancing seting chainlet'''


@appifies(KSlice)
class slicechain(LazyChainlet, AutoQMixin, SliceMixin):

    '''auto-balancing slicing chainlet'''


@appifies(KFilter)
class filterchain(LazyChainlet, AutoQMixin, FilterMixin):

    '''auto-balancing filtering chainlet'''


@appifies(KRandom)
class randomchain(LazyChainlet, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing chainlet'''


@appifies(KOrder)
class orderchain(LazyChainlet, AutoQMixin, OrderMixin):

    '''auto-balancing ordering chainlet'''


@appifies(KMath)
class mathchain(LazyChainlet, AutoQMixin, MathMixin):

    '''auto-balancing mathing chainlet'''


@appifies(KReduce)
class reducechain(LazyChainlet, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing chainlet'''


@appifies(KTruth)
class truthchain(LazyChainlet, AutoQMixin, TruthMixin):

    '''auto-balancing truthing chainlet'''
