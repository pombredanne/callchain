# -*- coding: utf-8 -*-
'''lazy manually balanced chainlet event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter

from callchain.lazy.chainlet import LazyEventletMixin

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


@appifies(KDelay)
class delayevent(LazyEventletMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping chainlet event chain'''


@appifies(KCopy)
class copyevent(LazyEventletMixin, ManQMixin, CopyMixin):

    '''manually balanced copy chainlet event chain'''


@appifies(KRepeat)
class repeatevent(LazyEventletMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat chainlet event chain'''


@appifies(KMap)
class mapevent(LazyEventletMixin, ManQMixin, MapMixin):

    '''manually balanced mapping chainlet event chain'''


@appifies(KCollect)
class collectevent(LazyEventletMixin, ManQMixin, CollectMixin):

    '''manually balanced collecting chainlet event chain'''


@appifies(KSet)
class setevent(LazyEventletMixin, ManQMixin, SetMixin):

    '''manually balanced seting chainlet event chain'''


@appifies(KSlice)
class sliceevent(LazyEventletMixin, ManQMixin, SliceMixin):

    '''manually balanced slicing chainlet event chain'''


@appifies(KFilter)
class filterevent(LazyEventletMixin, ManQMixin, FilterMixin):

    '''manually balanced filtering chainlet event chain'''


@appifies(KRandom)
class randomevent(LazyEventletMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing chainlet event chain'''


@appifies(KOrder)
class orderevent(LazyEventletMixin, ManQMixin, OrderMixin):

    '''manually balanced ordering chainlet event chain'''


@appifies(KMath)
class mathevent(LazyEventletMixin, ManQMixin, MathMixin):

    '''manually balanced mathing chainlet event chain'''


@appifies(KReduce)
class reduceevent(LazyEventletMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing chainlet event chain'''


@appifies(KTruth)
class truthevent(LazyEventletMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing chainlet event chain'''
