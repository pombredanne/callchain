# -*- coding: utf-8 -*-
'''active auto-balancing linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.linked import ActiveLinkQMixin
from callchain.chains.keys.order import KRandom, KOrder
from callchain.chains.keys.reduce import KMath, KReduce, KTruth
from callchain.chains.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.chains.keys.filter import KCollect, KSet, KSlice, KFilter

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(ActiveLinkQMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping linked chain'''


@appifies(KCopy)
class copychain(ActiveLinkQMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy linked chain'''


@appifies(KRepeat)
class repeatchain(ActiveLinkQMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat linked chain'''


@appifies(KMap)
class mapchain(ActiveLinkQMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping linked chain'''


@appifies(KCollect)
class collectchain(ActiveLinkQMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked chain'''


@appifies(KSet)
class setchain(ActiveLinkQMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked chain'''


@appifies(KSlice)
class slicechain(ActiveLinkQMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked chain'''


@appifies(KFilter)
class filterchain(ActiveLinkQMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked chain'''


@appifies(KRandom)
class randomchain(ActiveLinkQMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked chain'''


@appifies(KOrder)
class orderchain(ActiveLinkQMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked chain'''


@appifies(KMath)
class mathchain(ActiveLinkQMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing linked chain'''


@appifies(KReduce)
class reducechain(ActiveLinkQMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing linked chain'''


@appifies(KTruth)
class truthchain(ActiveLinkQMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing linked chain'''
