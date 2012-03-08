# -*- coding: utf-8 -*-
'''active auto-balancing chainlet event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter

from callchain.active.mixins import ActiveELetMixin

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


@appifies(KDelay)
class delayevent(ActiveELetMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping chainlet event chain'''


@appifies(KCopy)
class copyevent(ActiveELetMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy chainlet event chain'''


@appifies(KRepeat)
class repeatevent(ActiveELetMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat chainlet event chain'''


@appifies(KMap)
class mapevent(ActiveELetMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping chainlet event chain'''


@appifies(KCollect)
class collectevent(ActiveELetMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting chainlet event chain'''


@appifies(KSet)
class setevent(ActiveELetMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting chainlet event chain'''


@appifies(KSlice)
class sliceevent(ActiveELetMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing chainlet event chain'''


@appifies(KFilter)
class filterevent(ActiveELetMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering chainlet event chain'''


@appifies(KRandom)
class randomevent(ActiveELetMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing chainlet event chain'''


@appifies(KOrder)
class orderevent(ActiveELetMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering chainlet event chain'''


@appifies(KMath)
class mathevent(ActiveELetMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing chainlet event chain'''


@appifies(KReduce)
class reduceevent(ActiveELetMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing chainlet event chain'''


@appifies(KTruth)
class truthevent(ActiveELetMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing chainlet event chain'''