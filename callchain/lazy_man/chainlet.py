# -*- coding: utf-8 -*-
'''lazy manually balanced chainlets'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chainlet import LazyChainletQ
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
class delaychain(LazyChainletQ, ManQMixin, DelayMixin):

    '''manually balanced delayed map chainlet'''


@appifies(KCopy)
class copychain(LazyChainletQ, ManQMixin, CopyMixin):

    '''manually balanced copy chainlet'''


@appifies(KRepeat)
class repeatchain(LazyChainletQ, ManQMixin, RepeatMixin):

    '''manually balanced repeat chainlet'''


@appifies(KMap)
class mapchain(LazyChainletQ, ManQMixin, MapMixin):

    '''manually balanced map chainlet'''


@appifies(KCollect)
class collectchain(LazyChainletQ, ManQMixin, CollectMixin):

    '''manually balanced collect chainlet'''


@appifies(KSet)
class setchain(LazyChainletQ, ManQMixin, SetMixin):

    '''manually balanced set chainlet'''


@appifies(KSlice)
class slicechain(LazyChainletQ, ManQMixin, SliceMixin):

    '''manually balanced slice chainlet'''


@appifies(KFilter)
class filterchain(LazyChainletQ, ManQMixin, FilterMixin):

    '''manually balanced filter chainlet'''


@appifies(KRandom)
class randomchain(LazyChainletQ, ManQMixin, RandomMixin):

    '''manually balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(LazyChainletQ, ManQMixin, OrderMixin):

    '''manually balanced order chainlet'''


@appifies(KMath)
class mathchain(LazyChainletQ, ManQMixin, MathMixin):

    '''manually balanced math chainlet'''


@appifies(KReduce)
class reducechain(LazyChainletQ, ManQMixin, ReduceMixin):

    '''manually balanced reduce chainlet'''


@appifies(KTruth)
class truthchain(LazyChainletQ, ManQMixin, TruthMixin):

    '''manually balanced truth chainlet'''
