# -*- coding: utf-8 -*-
'''active manually balanced eventlets'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.services.order import KRandom, KOrder
from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.services.map import KDelay, KCopy, KRepeat, KMap
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

from callchain.active.mixins import ActiveEventlet

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


class ManActiveEventlet(ActiveEventlet, ManQMixin):

    '''active manually balanced eventlet'''


@appifies(KDelay)
class delayevent(ManActiveEventlet, DelayMixin):

    '''manually balanced delayed mapping eventlet'''


@appifies(KCopy)
class copyevent(ManActiveEventlet, CopyMixin):

    '''manually balanced copy eventlet'''


@appifies(KRepeat)
class repeatevent(ManActiveEventlet, RepeatMixin):

    '''manually balanced repeat eventlet'''


@appifies(KMap)
class mapevent(ManActiveEventlet, MapMixin):

    '''manually balanced mapping eventlet'''


@appifies(KCollect)
class collectevent(ManActiveEventlet, CollectMixin):

    '''manually balanced collecting eventlet'''


@appifies(KSet)
class setevent(ManActiveEventlet, SetMixin):

    '''manually balanced seting eventlet'''


@appifies(KSlice)
class sliceevent(ManActiveEventlet, SliceMixin):

    '''manually balanced slicing eventlet'''


@appifies(KFilter)
class filterevent(ManActiveEventlet, FilterMixin):

    '''manually balanced filtering eventlet'''


@appifies(KRandom)
class randomevent(ManActiveEventlet, RandomMixin):

    '''manually balanced randomizing eventlet'''


@appifies(KOrder)
class orderevent(ManActiveEventlet, OrderMixin):

    '''manually balanced ordering eventlet'''


@appifies(KMath)
class mathevent(ManActiveEventlet, MathMixin):

    '''manually balanced mathing eventlet'''


@appifies(KReduce)
class reduceevent(ManActiveEventlet, ReduceMixin):

    '''manually balanced reducing eventlet'''


@appifies(KTruth)
class truthevent(ManActiveEventlet, TruthMixin):

    '''manually balanced truthing eventlet'''
