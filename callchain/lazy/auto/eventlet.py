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


class AutoLazyEventlet(LazyEventlet, ManQMixin):

    '''manually balanced lazy eventlet'''


@appifies(KDelay)
class delayevent(AutoLazyEventlet, DelayMixin):

    '''manually balanced delayed mapping eventlet'''


@appifies(KCopy)
class copyevent(AutoLazyEventlet, CopyMixin):

    '''manually balanced copy eventlet'''


@appifies(KRepeat)
class repeatevent(AutoLazyEventlet, RepeatMixin):

    '''manually balanced repeat eventlet'''


@appifies(KMap)
class mapevent(AutoLazyEventlet, MapMixin):

    '''manually balanced mapping eventlet'''


@appifies(KCollect)
class collectevent(AutoLazyEventlet, CollectMixin):

    '''manually balanced collecting eventlet'''


@appifies(KSet)
class setevent(AutoLazyEventlet, SetMixin):

    '''manually balanced seting eventlet'''


@appifies(KSlice)
class sliceevent(AutoLazyEventlet, SliceMixin):

    '''manually balanced slicing eventlet'''


@appifies(KFilter)
class filterevent(AutoLazyEventlet, FilterMixin):

    '''manually balanced filtering eventlet'''


@appifies(KRandom)
class randomevent(AutoLazyEventlet, RandomMixin):

    '''manually balanced randomizing eventlet'''


@appifies(KOrder)
class orderevent(AutoLazyEventlet, OrderMixin):

    '''manually balanced ordering eventlet'''


@appifies(KMath)
class mathevent(AutoLazyEventlet, MathMixin):

    '''manually balanced mathing eventlet'''


@appifies(KReduce)
class reduceevent(AutoLazyEventlet, ReduceMixin):

    '''manually balanced reducing eventlet'''


@appifies(KTruth)
class truthevent(AutoLazyEventlet, TruthMixin):

    '''manually balanced truthing eventlet'''
