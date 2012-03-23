# -*- coding: utf-8 -*-
'''lazy manually balanced chainlets'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManMixin
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
class delaychain(ChainletQ, ManMixin, DelayMixin):

    '''manually balanced delayed mapping chainlet'''


@appifies(KFinger)
class fingerchain(ChainletQ, ManMixin, FingerMixin):

    '''manually balanced fingering chainlet'''


@appifies(KResults)
class resultchain(ChainletQ, ManMixin, ResultMixin):

    '''manually balanced results chainlet'''


@appifies(KCallable)
class callablechain(ChainletQ, ManMixin, CallableMixin):

    '''manually balanced callable chainlet'''


@appifies(KRepeat)
class repeatchain(ChainletQ, ManMixin, RepeatMixin):

    '''manually balanced repeat chainlet'''


@appifies(KMap)
class mapchain(ChainletQ, ManMixin, MapMixin):

    '''manually balanced mapping chainlet'''


@appifies(KCollect)
class collectchain(ChainletQ, ManMixin, CollectMixin):

    '''manually balanced collecting chainlet'''


@appifies(KSet)
class setchain(ChainletQ, ManMixin, SetMixin):

    '''manually balanced setting chainlet'''


@appifies(KSlice)
class slicechain(ChainletQ, ManMixin, SliceMixin):

    '''manually balanced slicing chainlet'''


@appifies(KFilter)
class filterchain(ChainletQ, ManMixin, FilterMixin):

    '''manually balanced filtering chainlet'''


@appifies(KRandom)
class randomchain(ChainletQ, ManMixin, RandomMixin):

    '''manually balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(ChainletQ, ManMixin, OrderMixin):

    '''manually balanced ordering chainlet'''


@appifies(KMath)
class mathchain(ChainletQ, ManMixin, MathMixin):

    '''manually balanced mathing chainlet'''


@appifies(KReduce)
class reducechain(ChainletQ, ManMixin, ReduceMixin):

    '''manually balanced reducing chainlet'''


@appifies(KTruth)
class truthchain(ChainletQ, ManMixin, TruthMixin):

    '''manually balanced truthing chainlet'''
