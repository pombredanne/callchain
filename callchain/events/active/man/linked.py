# -*- coding: utf-8 -*-
'''active manually balanced linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
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
class delayevent(EventLinkMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping linked event chain'''


@appifies(KCopy)
class copyevent(EventLinkMixin, ManQMixin, CopyMixin):

    '''manually balanced copy linked event chain'''


@appifies(KRepeat)
class repeatevent(EventLinkMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat linked event chain'''


@appifies(KMap)
class mapevent(EventLinkMixin, ManQMixin, MapMixin):

    '''manually balanced mapping linked event chain'''


@appifies(KCollect)
class collectevent(EventLinkMixin, ManQMixin, CollectMixin):

    '''manually balanced collecting linked event chain'''


@appifies(KSet)
class setevent(EventLinkMixin, ManQMixin, SetMixin):

    '''manually balanced seting linked event chain'''


@appifies(KSlice)
class sliceevent(EventLinkMixin, ManQMixin, SliceMixin):

    '''manually balanced slicing linked event chain'''


@appifies(KFilter)
class filterevent(EventLinkMixin, ManQMixin, FilterMixin):

    '''manually balanced filtering linked event chain'''


@appifies(KRandom)
class randomevent(EventLinkMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing linked event chain'''


@appifies(KOrder)
class orderevent(EventLinkMixin, ManQMixin, OrderMixin):

    '''manually balanced ordering linked event chain'''


@appifies(KMath)
class mathevent(EventLinkMixin, ManQMixin, MathMixin):

    '''manually balanced mathing linked event chain'''


@appifies(KReduce)
class reduceevent(EventLinkMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing linked event chain'''


@appifies(KTruth)
class truthevent(EventLinkMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing linked event chain'''
