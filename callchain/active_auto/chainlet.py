# -*- coding: utf-8 -*-
'''active auto-balancing chainlets'''

from appspace.keys import appifies
from twoq.active.mixins import AutoMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.queuing import ResultMixin, FingerMixin, CallableMixin

from callchain.chain import ChainletQ
from callchain.services.order import KRandom, KOrder
from callchain.services.queue import KFinger, KResults, KCallable
from callchain.services.map import KDelay, KRepeat, KMap
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'repeatchain', 'mapchain',
    'randomchain', 'orderchain', 'fingerchain', 'resultchain', 'callablechain',
)


@appifies(KDelay)
class delaychain(ChainletQ, AutoMixin, DelayMixin):

    '''auto-balancing delayed mapping chainlet'''


@appifies(KFinger)
class fingerchain(ChainletQ, AutoMixin, FingerMixin):

    '''auto-balancing fingering chainlet'''


@appifies(KResults)
class resultchain(ChainletQ, AutoMixin, ResultMixin):

    '''auto-balancing results chainlet'''


@appifies(KCallable)
class callablechain(ChainletQ, AutoMixin, CallableMixin):

    '''auto-balancing callable chainlet'''


@appifies(KRepeat)
class repeatchain(ChainletQ, AutoMixin, RepeatMixin):

    '''auto-balancing repeat chainlet'''


@appifies(KMap)
class mapchain(ChainletQ, AutoMixin, MapMixin):

    '''auto-balancing mapping chainlet'''


@appifies(KCollect)
class collectchain(ChainletQ, AutoMixin, CollectMixin):

    '''auto-balancing collecting chainlet'''


@appifies(KSet)
class setchain(ChainletQ, AutoMixin, SetMixin):

    '''auto-balancing seting chainlet'''


@appifies(KSlice)
class slicechain(ChainletQ, AutoMixin, SliceMixin):

    '''auto-balancing slicing chainlet'''


@appifies(KFilter)
class filterchain(ChainletQ, AutoMixin, FilterMixin):

    '''auto-balancing filtering chainlet'''


@appifies(KRandom)
class randomchain(ChainletQ, AutoMixin, RandomMixin):

    '''auto-balancing randomizing chainlet'''


@appifies(KOrder)
class orderchain(ChainletQ, AutoMixin, OrderMixin):

    '''auto-balancing ordering chainlet'''


@appifies(KMath)
class mathchain(ChainletQ, AutoMixin, MathMixin):

    '''auto-balancing mathing chainlet'''


@appifies(KReduce)
class reducechain(ChainletQ, AutoMixin, ReduceMixin):

    '''auto-balancing reducing chainlet'''


@appifies(KTruth)
class truthchain(ChainletQ, AutoMixin, TruthMixin):

    '''auto-balancing truthing chainlet'''
