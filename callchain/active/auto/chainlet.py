# -*- coding: utf-8 -*-
'''active auto-balancing chainlets'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter

from callchain.active.linked import ActiveChainletMixin

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'copychain', 'repeatchain',
    'mapchain', 'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(ActiveChainletMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping chainlet'''


@appifies(KCopy)
class copychain(ActiveChainletMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy chainlet'''


@appifies(KRepeat)
class repeatchain(ActiveChainletMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat chainlet'''


@appifies(KMap)
class mapchain(ActiveChainletMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping chainlet'''


@appifies(KCollect)
class collectchain(ActiveChainletMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting chainlet'''


@appifies(KSet)
class setchain(ActiveChainletMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting chainlet'''


@appifies(KSlice)
class slicechain(ActiveChainletMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing chainlet'''


@appifies(KFilter)
class filterchain(ActiveChainletMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering chainlet'''


@appifies(KRandom)
class randomchain(ActiveChainletMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing chainlet'''


@appifies(KOrder)
class orderchain(ActiveChainletMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering chainlet'''


@appifies(KMath)
class mathchain(ActiveChainletMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing chainlet'''


@appifies(KReduce)
class reducechain(ActiveChainletMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing chainlet'''


@appifies(KTruth)
class truthchain(ActiveChainletMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing chainlet'''
