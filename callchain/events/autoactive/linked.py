# -*- coding: utf-8 -*-
'''active auto-balancing linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.keys.order import KRandom, KOrder
from callchain.chains.keys.reduce import KMath, KReduce, KTruth
from callchain.chains.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.chains.keys.filter import KCollect, KSet, KSlice, KFilter
from callchain.events.linked import ActiveELinkedQMixin

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


@appifies(KDelay)
class delayevent(ActiveELinkedQMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping linked event chain'''


@appifies(KCopy)
class copyevent(ActiveELinkedQMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy linked event chain'''


@appifies(KRepeat)
class repeatevent(ActiveELinkedQMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat linked event chain'''


@appifies(KMap)
class mapevent(ActiveELinkedQMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping linked event chain'''


@appifies(KCollect)
class collectevent(ActiveELinkedQMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked event chain'''


@appifies(KSet)
class setevent(ActiveELinkedQMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked event chain'''


@appifies(KSlice)
class sliceevent(ActiveELinkedQMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked event chain'''


@appifies(KFilter)
class filterevent(ActiveELinkedQMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked event chain'''


@appifies(KRandom)
class randomevent(ActiveELinkedQMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked event chain'''


@appifies(KOrder)
class orderevent(ActiveELinkedQMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked event chain'''


@appifies(KMath)
class mathevent(ActiveELinkedQMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing linked event chain'''


@appifies(KReduce)
class reduceevent(ActiveELinkedQMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing linked event chain'''


@appifies(KTruth)
class truthevent(ActiveELinkedQMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing linked event chain'''
