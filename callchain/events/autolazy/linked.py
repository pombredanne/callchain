# -*- coding: utf-8 -*-
'''lazy manually balanced linked event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.keys.order import KRandom, KOrder
from callchain.chains.keys.reduce import KMath, KReduce, KTruth
from callchain.chains.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.chains.keys.filter import KCollect, KSet, KSlice, KFilter

from callchain.events.queue import LazyEventLinkMixin

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


@appifies(KDelay)
class delayevent(LazyEventLinkMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping linked event chain'''


@appifies(KCopy)
class copyevent(LazyEventLinkMixin, ManQMixin, CopyMixin):

    '''manually balanced copy linked event chain'''


@appifies(KRepeat)
class repeatevent(LazyEventLinkMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat linked event chain'''


@appifies(KMap)
class mapevent(LazyEventLinkMixin, ManQMixin, MapMixin):

    '''manually balanced mapping linked event chain'''


@appifies(KCollect)
class collectevent(LazyEventLinkMixin, ManQMixin, CollectMixin):

    '''manually balanced collecting linked event chain'''


@appifies(KSet)
class setevent(LazyEventLinkMixin, ManQMixin, SetMixin):

    '''manually balanced seting linked event chain'''


@appifies(KSlice)
class sliceevent(LazyEventLinkMixin, ManQMixin, SliceMixin):

    '''manually balanced slicing linked event chain'''


@appifies(KFilter)
class filterevent(LazyEventLinkMixin, ManQMixin, FilterMixin):

    '''manually balanced filtering linked event chain'''


@appifies(KRandom)
class randomevent(LazyEventLinkMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing linked event chain'''


@appifies(KOrder)
class orderevent(LazyEventLinkMixin, ManQMixin, OrderMixin):

    '''manually balanced ordering linked event chain'''


@appifies(KMath)
class mathevent(LazyEventLinkMixin, ManQMixin, MathMixin):

    '''manually balanced mathing linked event chain'''


@appifies(KReduce)
class reduceevent(LazyEventLinkMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing linked event chain'''


@appifies(KTruth)
class truthevent(LazyEventLinkMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing linked event chain'''
