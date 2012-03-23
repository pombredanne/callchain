# -*- coding: utf-8 -*-
'''lazy manually balanced chainlets'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.chain import ChainletQ
from callchain.services.order import KRandom, KOrder
from callchain.services.map import KDelay, KRepeat, KMap
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'repeatchain', 'mapchain',
    'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(ChainletQ, ManQMixin, DelayMixin):

    '''manually balanced delayed map chainlet'''


@appifies(KRepeat)
class repeatchain(ChainletQ, ManQMixin, RepeatMixin):

    '''manually balanced repeat chainlet'''


@appifies(KMap)
class mapchain(ChainletQ, ManQMixin, MapMixin):

    '''manually balanced map chainlet'''


@appifies(KCollect)
class collectchain(ChainletQ, ManQMixin, CollectMixin):

    '''manually balanced collect chainlet'''


@appifies(KSet)
class setchain(ChainletQ, ManQMixin, SetMixin):

    '''manually balanced set chainlet'''


@appifies(KSlice)
class slicechain(ChainletQ, ManQMixin, SliceMixin):

    '''manually balanced slice chainlet'''


@appifies(KFilter)
class filterchain(ChainletQ, ManQMixin, FilterMixin):

    '''manually balanced filter chainlet'''


@appifies(KRandom)
class randomchain(ChainletQ, ManQMixin, RandomMixin):

    '''manually balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(ChainletQ, ManQMixin, OrderMixin):

    '''manually balanced order chainlet'''


@appifies(KMath)
class mathchain(ChainletQ, ManQMixin, MathMixin):

    '''manually balanced math chainlet'''


@appifies(KReduce)
class reducechain(ChainletQ, ManQMixin, ReduceMixin):

    '''manually balanced reduce chainlet'''


@appifies(KTruth)
class truthchain(ChainletQ, ManQMixin, TruthMixin):

    '''manually balanced truth chainlet'''
