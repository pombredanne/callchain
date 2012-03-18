# -*- coding: utf-8 -*-
'''active manually balanced chainlets'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.services.order import KRandom, KOrder
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.services.map import KDelay, KCopy, KRepeat, KMap
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

from callchain.active.mixins import ActiveChainlet

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


class AutoActiveChainlet(ActiveChainlet, ManQMixin):

    '''active manually balanced eventlet'''


@appifies(KDelay)
class delaychain(AutoActiveChainlet, DelayMixin):

    '''manually balanced delayed mapping chainlet'''


@appifies(KCopy)
class copychain(AutoActiveChainlet, CopyMixin):

    '''manually balanced copy chainlet'''


@appifies(KRepeat)
class repeatchain(AutoActiveChainlet, RepeatMixin):

    '''manually balanced repeat chainlet'''


@appifies(KMap)
class mapchain(AutoActiveChainlet, MapMixin):

    '''manually balanced mapping chainlet'''


@appifies(KCollect)
class collectchain(AutoActiveChainlet, CollectMixin):

    '''manually balanced collecting chainlet'''


@appifies(KSet)
class setchain(AutoActiveChainlet, SetMixin):

    '''manually balanced seting chainlet'''


@appifies(KSlice)
class slicechain(AutoActiveChainlet, SliceMixin):

    '''manually balanced slicing chainlet'''


@appifies(KFilter)
class filterchain(AutoActiveChainlet, FilterMixin):

    '''manually balanced filtering chainlet'''


@appifies(KRandom)
class randomchain(AutoActiveChainlet, RandomMixin):

    '''manually balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(AutoActiveChainlet, OrderMixin):

    '''manually balanced ordering chainlet'''


@appifies(KMath)
class mathchain(AutoActiveChainlet, MathMixin):

    '''manually balanced mathing chainlet'''


@appifies(KReduce)
class reducechain(AutoActiveChainlet, ReduceMixin):

    '''manually balanced reducing chainlet'''


@appifies(KTruth)
class truthchain(AutoActiveChainlet, TruthMixin):

    '''manually balanced truthing chainlet'''
