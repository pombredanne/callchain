# -*- coding: utf-8 -*-
'''lazy manually balanced linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.linked import LazyLinkQMixin
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
class delaychain(LazyLinkQMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed map linked chain'''


@appifies(KCopy)
class copychain(LazyLinkQMixin, ManQMixin, CopyMixin):

    '''manually balanced copy linked chain'''


@appifies(KRepeat)
class repeatchain(LazyLinkQMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat linked chain'''


@appifies(KMap)
class mapchain(LazyLinkQMixin, ManQMixin, MapMixin):

    '''manually balanced map linked chain'''


@appifies(KCollect)
class collectchain(LazyLinkQMixin, ManQMixin, CollectMixin):

    '''manually balanced collect linked chain'''


@appifies(KSet)
class setchain(LazyLinkQMixin, ManQMixin, SetMixin):

    '''manually balanced set linked chain'''


@appifies(KSlice)
class slicechain(LazyLinkQMixin, ManQMixin, SliceMixin):

    '''manually balanced slice linked chain'''


@appifies(KFilter)
class filterchain(LazyLinkQMixin, ManQMixin, FilterMixin):

    '''manually balanced filter linked chain'''


@appifies(KRandom)
class randomchain(LazyLinkQMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing linked chain'''


@appifies(KOrder)
class orderchain(LazyLinkQMixin, ManQMixin, OrderMixin):

    '''manually balanced order linked chain'''


@appifies(KMath)
class mathchain(LazyLinkQMixin, ManQMixin, MathMixin):

    '''manually balanced math linked chain'''


@appifies(KReduce)
class reducechain(LazyLinkQMixin, ManQMixin, ReduceMixin):

    '''manually balanced reduce linked chain'''


@appifies(KTruth)
class truthchain(LazyLinkQMixin, ManQMixin, TruthMixin):

    '''manually balanced truth linked chain'''
