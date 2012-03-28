# -*- coding: utf-8 -*-
'''active auto-balancing chainlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.active.mixins import AutoQMixin, AutoResultMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.keys.call import KCall
from callchain.keys.root import KConfig
from callchain.keys.core import KChainKey
from callchain.keys.branch import KLinkedKey
from callchain.chain import Chainlet, Linked
from callchain.services.queue import KResult
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
class delaychain(Chainlet, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping chainlet'''


@appifies(KRepeat)
class repeatchain(Chainlet, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat chainlet'''


@appifies(KMap)
class mapchain(Chainlet, AutoQMixin, MapMixin):

    '''auto-balancing mapping chainlet'''


@appifies(KCollect)
class collectchain(Chainlet, AutoQMixin, CollectMixin):

    '''auto-balancing collecting chainlet'''


@appifies(KSet)
class setchain(Chainlet, AutoQMixin, SetMixin):

    '''auto-balancing seting chainlet'''


@appifies(KSlice)
class slicechain(Chainlet, AutoQMixin, SliceMixin):

    '''auto-balancing slicing chainlet'''


@appifies(KFilter)
class filterchain(Chainlet, AutoQMixin, FilterMixin):

    '''auto-balancing filtering chainlet'''


@appifies(KRandom)
class randomchain(Chainlet, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing chainlet'''


@appifies(KOrder)
class orderchain(Chainlet, AutoQMixin, OrderMixin):

    '''auto-balancing ordering chainlet'''


@appifies(KMath)
class mathchain(Chainlet, AutoQMixin, MathMixin):

    '''auto-balancing mathing chainlet'''


@appifies(KReduce)
class reducechain(Chainlet, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing chainlet'''


@appifies(KTruth)
class truthchain(Chainlet, AutoQMixin, TruthMixin):

    '''auto-balancing truthing chainlet'''


@appifies(KLinkedKey, KConfig, KCall, KChainKey, KResult)
class chainlink(Linked, AutoResultMixin):

    '''auto-balancing linked chain'''
