# -*- coding: utf-8 -*-
'''active auto-balancing linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.services.order import KRandom, KOrder
from callchain.chains.services.reduce import KMath, KReduce, KTruth
from callchain.chains.services.map import KDelay, KCopy, KRepeat, KMap
from callchain.chains.services.filter import KCollect, KSet, KSlice, KFilter

from callchain.events.active.queue import EventLinkMixin

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


@appifies(KDelay)
class delayevent(EventLinkMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping linked event chain'''


@appifies(KCopy)
class copyevent(EventLinkMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy linked event chain'''


@appifies(KRepeat)
class repeatevent(EventLinkMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat linked event chain'''


@appifies(KMap)
class mapevent(EventLinkMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping linked event chain'''


@appifies(KCollect)
class collectevent(EventLinkMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked event chain'''


@appifies(KSet)
class setevent(EventLinkMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked event chain'''


@appifies(KSlice)
class sliceevent(EventLinkMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked event chain'''


@appifies(KFilter)
class filterevent(EventLinkMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked event chain'''


@appifies(KRandom)
class randomevent(EventLinkMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked event chain'''


@appifies(KOrder)
class orderevent(EventLinkMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked event chain'''


@appifies(KMath)
class mathevent(EventLinkMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing linked event chain'''


@appifies(KReduce)
class reduceevent(EventLinkMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing linked event chain'''


@appifies(KTruth)
class truthevent(EventLinkMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing linked event chain'''
