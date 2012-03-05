# -*- coding: utf-8 -*-
'''lazy auto-balancing linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.lazy.queue import ChainLinkMixin
from callchain.chains.services.order import KRandom, KOrder
from callchain.chains.services.reduce import KMath, KReduce, KTruth
from callchain.chains.services.map import KDelay, KCopy, KRepeat, KMap
from callchain.chains.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(ChainLinkMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping linked chain'''


@appifies(KCopy)
class copychain(ChainLinkMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy linked chain'''


@appifies(KRepeat)
class repeatchain(ChainLinkMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat linked chain'''


@appifies(KMap)
class mapchain(ChainLinkMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping linked chain'''


@appifies(KCollect)
class collectchain(ChainLinkMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked chain'''


@appifies(KSet)
class setchain(ChainLinkMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked chain'''


@appifies(KSlice)
class slicechain(ChainLinkMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked chain'''


@appifies(KFilter)
class filterchain(ChainLinkMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked chain'''


@appifies(KRandom)
class randomchain(ChainLinkMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked chain'''


@appifies(KOrder)
class orderchain(ChainLinkMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked chain'''


@appifies(KMath)
class mathchain(ChainLinkMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing linked chain'''


@appifies(KReduce)
class reducechain(ChainLinkMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing linked chain'''


@appifies(KTruth)
class truthchain(ChainLinkMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing linked chain'''
