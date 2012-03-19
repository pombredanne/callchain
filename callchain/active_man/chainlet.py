# -*- coding: utf-8 -*-
'''active manually balanced chainlets'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chain import ChainletQ
from callchain.services.order import KRandom, KOrder
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.services.map import KDelay, KCopy, KRepeat, KMap
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(ChainletQ, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping chainlet'''


@appifies(KCopy)
class copychain(ChainletQ, ManQMixin, CopyMixin):

    '''manually balanced copy chainlet'''


@appifies(KRepeat)
class repeatchain(ChainletQ, ManQMixin, RepeatMixin):

    '''manually balanced repeat chainlet'''


@appifies(KMap)
class mapchain(ChainletQ, ManQMixin, MapMixin):

    '''manually balanced mapping chainlet'''


@appifies(KCollect)
class collectchain(ChainletQ, ManQMixin, CollectMixin):

    '''manually balanced collecting chainlet'''


@appifies(KSet)
class setchain(ChainletQ, ManQMixin, SetMixin):

    '''manually balanced seting chainlet'''


@appifies(KSlice)
class slicechain(ChainletQ, ManQMixin, SliceMixin):

    '''manually balanced slicing chainlet'''


@appifies(KFilter)
class filterchain(ChainletQ, ManQMixin, FilterMixin):

    '''manually balanced filtering chainlet'''


@appifies(KRandom)
class randomchain(ChainletQ, ManQMixin, RandomMixin):

    '''manually balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(ChainletQ, ManQMixin, OrderMixin):

    '''manually balanced ordering chainlet'''


@appifies(KMath)
class mathchain(ChainletQ, ManQMixin, MathMixin):

    '''manually balanced mathing chainlet'''


@appifies(KReduce)
class reducechain(ChainletQ, ManQMixin, ReduceMixin):

    '''manually balanced reducing chainlet'''


@appifies(KTruth)
class truthchain(ChainletQ, ManQMixin, TruthMixin):

    '''manually balanced truthing chainlet'''
