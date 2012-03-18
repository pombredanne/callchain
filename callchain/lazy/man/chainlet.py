# -*- coding: utf-8 -*-
'''lazy manually balanced chainlets'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
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


class ManLazyChainlet(LazyChainlet, ManQMixin):

    '''active manually balanced eventlet'''


@appifies(KDelay)
class delaychain(ManLazyChainlet, DelayMixin):

    '''manually balanced delayed map chainlet'''


@appifies(KCopy)
class copychain(ManLazyChainlet, CopyMixin):

    '''manually balanced copy chainlet'''


@appifies(KRepeat)
class repeatchain(ManLazyChainlet, RepeatMixin):

    '''manually balanced repeat chainlet'''


@appifies(KMap)
class mapchain(ManLazyChainlet, MapMixin):

    '''manually balanced map chainlet'''


@appifies(KCollect)
class collectchain(ManLazyChainlet, CollectMixin):

    '''manually balanced collect chainlet'''


@appifies(KSet)
class setchain(ManLazyChainlet, SetMixin):

    '''manually balanced set chainlet'''


@appifies(KSlice)
class slicechain(ManLazyChainlet, SliceMixin):

    '''manually balanced slice chainlet'''


@appifies(KFilter)
class filterchain(ManLazyChainlet, FilterMixin):

    '''manually balanced filter chainlet'''


@appifies(KRandom)
class randomchain(ManLazyChainlet, RandomMixin):

    '''manually balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(ManLazyChainlet, OrderMixin):

    '''manually balanced order chainlet'''


@appifies(KMath)
class mathchain(ManLazyChainlet, MathMixin):

    '''manually balanced math chainlet'''


@appifies(KReduce)
class reducechain(ManLazyChainlet, ReduceMixin):

    '''manually balanced reduce chainlet'''


@appifies(KTruth)
class truthchain(ManLazyChainlet, TruthMixin):

    '''manually balanced truth chainlet'''
