# -*- coding: utf-8 -*-
'''lazy manually balanced linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
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
class delaychain(ChainLinkMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed map linked chain'''


@appifies(KCopy)
class copychain(ChainLinkMixin, ManQMixin, CopyMixin):

    '''manually balanced copy linked chain'''


@appifies(KRepeat)
class repeatchain(ChainLinkMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat linked chain'''


@appifies(KMap)
class mapchain(ChainLinkMixin, ManQMixin, MapMixin):

    '''manually balanced map linked chain'''


@appifies(KCollect)
class collectchain(ChainLinkMixin, ManQMixin, CollectMixin):

    '''manually balanced collect linked chain'''


@appifies(KSet)
class setchain(ChainLinkMixin, ManQMixin, SetMixin):

    '''manually balanced set linked chain'''


@appifies(KSlice)
class slicechain(ChainLinkMixin, ManQMixin, SliceMixin):

    '''manually balanced slice linked chain'''


@appifies(KFilter)
class filterchain(ChainLinkMixin, ManQMixin, FilterMixin):

    '''manually balanced filter linked chain'''


@appifies(KRandom)
class randomchain(ChainLinkMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing linked chain'''


@appifies(KOrder)
class orderchain(ChainLinkMixin, ManQMixin, OrderMixin):

    '''manually balanced order linked chain'''


@appifies(KMath)
class mathchain(ChainLinkMixin, ManQMixin, MathMixin):

    '''manually balanced math linked chain'''


@appifies(KReduce)
class reducechain(ChainLinkMixin, ManQMixin, ReduceMixin):

    '''manually balanced reduce linked chain'''


@appifies(KTruth)
class truthchain(ChainLinkMixin, ManQMixin, TruthMixin):

    '''manually balanced truth linked chain'''
