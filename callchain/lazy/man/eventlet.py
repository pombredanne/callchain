# -*- coding: utf-8 -*-
'''lazy manually balanced eventlets'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter

from callchain.lazy.mixins import LazyEventlet

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


class ManLazyEventlet(LazyEventlet, ManQMixin):

    '''active manually balanced eventlet'''


@appifies(KDelay)
class delayevent(ManLazyEventlet, DelayMixin):

    '''manually balanced delayed mapping eventlet'''


@appifies(KCopy)
class copyevent(ManLazyEventlet, CopyMixin):

    '''manually balanced copy eventlet'''


@appifies(KRepeat)
class repeatevent(ManLazyEventlet, RepeatMixin):

    '''manually balanced repeat eventlet'''


@appifies(KMap)
class mapevent(ManLazyEventlet, MapMixin):

    '''manually balanced mapping eventlet'''


@appifies(KCollect)
class collectevent(ManLazyEventlet, CollectMixin):

    '''manually balanced collecting eventlet'''


@appifies(KSet)
class setevent(ManLazyEventlet, SetMixin):

    '''manually balanced seting eventlet'''


@appifies(KSlice)
class sliceevent(ManLazyEventlet, SliceMixin):

    '''manually balanced slicing eventlet'''


@appifies(KFilter)
class filterevent(ManLazyEventlet, FilterMixin):

    '''manually balanced filtering eventlet'''


@appifies(KRandom)
class randomevent(ManLazyEventlet, RandomMixin):

    '''manually balanced randomizing eventlet'''


@appifies(KOrder)
class orderevent(ManLazyEventlet, OrderMixin):

    '''manually balanced ordering eventlet'''


@appifies(KMath)
class mathevent(ManLazyEventlet, MathMixin):

    '''manually balanced mathing eventlet'''


@appifies(KReduce)
class reduceevent(ManLazyEventlet, ReduceMixin):

    '''manually balanced reducing eventlet'''


@appifies(KTruth)
class truthevent(ManLazyEventlet, TruthMixin):

    '''manually balanced truthing eventlet'''
