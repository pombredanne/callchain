# -*- coding: utf-8 -*-
'''lazy lazy balanced chainlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.lazy.mixins import AutoQMixin, AutoResultMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.mapping import DelayMixin, RepeatMixin, MapMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.keys.call import KCall
from callchain.keys.root import KConfig
from callchain.keys.core import KChainKey
from callchain.keys.branch import KLinkedKey
from callchain.chain import Chainlet, Linked
from callchain.services.order import KRandom, KOrder
from callchain.services.map import KDelay, KRepeat, KMap
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.services.filter import KCollect, KSet, KSlice, KFilter
from callchain.services.queue import KResult

__all__ = (
    'mathchain', 'truthchain', 'reducechain', 'collectchain', 'setchain',
    'slicechain', 'filterchain', 'delaychain', 'repeatchain', 'mapchain',
    'randomchain', 'orderchain',
)


@appifies(KDelay)
class delaychain(Chainlet, AutoQMixin, DelayMixin):

    '''lazy balanced delayed mapping chainlet'''


@appifies(KRepeat)
class repeatchain(Chainlet, AutoQMixin, RepeatMixin):

    '''lazy balanced repeat chainlet'''


@appifies(KMap)
class mapchain(Chainlet, AutoQMixin, MapMixin):

    '''lazy balanced mapping chainlet'''


@appifies(KCollect)
class collectchain(Chainlet, AutoQMixin, CollectMixin):

    '''lazy balanced collecting chainlet'''


@appifies(KSet)
class setchain(Chainlet, AutoQMixin, SetMixin):

    '''lazy balanced seting chainlet'''


@appifies(KSlice)
class slicechain(Chainlet, AutoQMixin, SliceMixin):

    '''lazy balanced slicing chainlet'''


@appifies(KFilter)
class filterchain(Chainlet, AutoQMixin, FilterMixin):

    '''lazy balanced filtering chainlet'''


@appifies(KRandom)
class randomchain(Chainlet, AutoQMixin, RandomMixin):

    '''lazy balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(Chainlet, AutoQMixin, OrderMixin):

    '''lazy balanced ordering chainlet'''


@appifies(KMath)
class mathchain(Chainlet, AutoQMixin, MathMixin):

    '''lazy balanced mathing chainlet'''


@appifies(KReduce)
class reducechain(Chainlet, AutoQMixin, ReduceMixin):

    '''lazy balanced reducing chainlet'''


@appifies(KTruth)
class truthchain(Chainlet, AutoQMixin, TruthMixin):

    '''lazy balanced truthing chainlet'''


@appifies(KLinkedKey, KConfig, KCall, KChainKey, KResult)
class chainlink(Linked, AutoResultMixin):

    '''lazy balanced linked chain'''
