# -*- coding: utf-8 -*-
'''active manually balanced linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.active.queue import ChainLinkMixin
from callchain.chains.services.order import KRandom, KOrder
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from callchain.chains.services.reduce import KMath, KReduce, KTruth
from callchain.chains.services.map import KDelay, KCopy, KRepeat, KMap
from callchain.chains.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(ChainLinkMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping linked chain'''


@appifies(KCopy)
class copychain(ChainLinkMixin, ManQMixin, CopyMixin):

    '''manually balanced copy linked chain'''


@appifies(KRepeat)
class repeatchain(ChainLinkMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat linked chain'''


@appifies(KMap)
class mapchain(ChainLinkMixin, ManQMixin, MapMixin):

    '''manually balanced mapping linked chain'''


@appifies(KCollect)
class collectchain(ChainLinkMixin, ManQMixin, CollectMixin):

    '''manually balanced collecting linked chain'''


@appifies(KSet)
class setchain(ChainLinkMixin, ManQMixin, SetMixin):

    '''manually balanced seting linked chain'''


@appifies(KSlice)
class slicechain(ChainLinkMixin, ManQMixin, SliceMixin):

    '''manually balanced slicing linked chain'''


@appifies(KFilter)
class filterchain(ChainLinkMixin, ManQMixin, FilterMixin):

    '''manually balanced filtering linked chain'''


@appifies(KRandom)
class randomchain(ChainLinkMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing linked chain'''


@appifies(KOrder)
class orderchain(ChainLinkMixin, ManQMixin, OrderMixin):

    '''manually balanced ordering linked chain'''


@appifies(KMath)
class mathchain(ChainLinkMixin, ManQMixin, MathMixin):

    '''manually balanced mathing linked chain'''


@appifies(KReduce)
class reducechain(ChainLinkMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing linked chain'''


@appifies(KTruth)
class truthchain(ChainLinkMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing linked chain'''
