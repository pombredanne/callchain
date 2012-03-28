# -*- coding: utf-8 -*-
'''active manually balanced chainlets'''

from appspace.keys import appifies
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.active.mixins import ManQMixin, ManResultMixin
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
class delaychain(Chainlet, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping chainlet'''


@appifies(KRepeat)
class repeatchain(Chainlet, ManQMixin, RepeatMixin):

    '''manually balanced repeat chainlet'''


@appifies(KMap)
class mapchain(Chainlet, ManQMixin, MapMixin):

    '''manually balanced mapping chainlet'''


@appifies(KCollect)
class collectchain(Chainlet, ManQMixin, CollectMixin):

    '''manually balanced collecting chainlet'''


@appifies(KSet)
class setchain(Chainlet, ManQMixin, SetMixin):

    '''manually balanced setting chainlet'''


@appifies(KSlice)
class slicechain(Chainlet, ManQMixin, SliceMixin):

    '''manually balanced slicing chainlet'''


@appifies(KFilter)
class filterchain(Chainlet, ManQMixin, FilterMixin):

    '''manually balanced filtering chainlet'''


@appifies(KRandom)
class randomchain(Chainlet, ManQMixin, RandomMixin):

    '''manually balanced randomizing chainlet'''


@appifies(KOrder)
class orderchain(Chainlet, ManQMixin, OrderMixin):

    '''manually balanced ordering chainlet'''


@appifies(KMath)
class mathchain(Chainlet, ManQMixin, MathMixin):

    '''manually balanced mathing chainlet'''


@appifies(KReduce)
class reducechain(Chainlet, ManQMixin, ReduceMixin):

    '''manually balanced reducing chainlet'''


@appifies(KTruth)
class truthchain(Chainlet, ManQMixin, TruthMixin):

    '''manually balanced truthing chainlet'''


@appifies(KLinkedKey, KConfig, KCall, KChainKey, KResult)
class chainlink(Linked, ManResultMixin):

    '''manually balanced linked chain'''
