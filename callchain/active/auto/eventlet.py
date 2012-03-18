# -*- coding: utf-8 -*-
'''active auto-balancing eventlets'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)
from twoq.mixins.ordering import RandomMixin, OrderMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.keys.order import KRandom, KOrder
from callchain.keys.reduce import KMath, KReduce, KTruth
from callchain.keys.map import KDelay, KCopy, KRepeat, KMap
from callchain.keys.filter import KCollect, KSet, KSlice, KFilter

from callchain.active.mixins import ActiveEventlet

__all__ = (
    'mathevent', 'truthevent', 'reduceevent', 'collectevent', 'setevent',
    'sliceevent', 'filterevent', 'delayevent', 'copyevent', 'repeatevent',
    'mapevent', 'randomevent', 'orderevent',
)


class AutoActiveChainlet(ActiveEventlet, AutoQMixin):

    '''active manually balanced eventlet'''


@appifies(KDelay)
class delayevent(AutoActiveChainlet, DelayMixin):

    '''auto-balancing delayed mapping eventlet'''


@appifies(KCopy)
class copyevent(AutoActiveChainlet, CopyMixin):

    '''auto-balancing copy eventlet'''


@appifies(KRepeat)
class repeatevent(AutoActiveChainlet, RepeatMixin):

    '''auto-balancing repeat eventlet'''


@appifies(KMap)
class mapevent(AutoActiveChainlet, MapMixin):

    '''auto-balancing mapping eventlet'''


@appifies(KCollect)
class collectevent(AutoActiveChainlet, CollectMixin):

    '''auto-balancing collecting eventlet'''


@appifies(KSet)
class setevent(AutoActiveChainlet, SetMixin):

    '''auto-balancing seting eventlet'''


@appifies(KSlice)
class sliceevent(AutoActiveChainlet, SliceMixin):

    '''auto-balancing slicing eventlet'''


@appifies(KFilter)
class filterevent(AutoActiveChainlet, FilterMixin):

    '''auto-balancing filtering eventlet'''


@appifies(KRandom)
class randomevent(AutoActiveChainlet, RandomMixin):

    '''auto-balancing randomizing eventlet'''


@appifies(KOrder)
class orderevent(AutoActiveChainlet, OrderMixin):

    '''auto-balancing ordering eventlet'''


@appifies(KMath)
class mathevent(AutoActiveChainlet, MathMixin):

    '''auto-balancing mathing eventlet'''


@appifies(KReduce)
class reduceevent(AutoActiveChainlet, ReduceMixin):

    '''auto-balancing reducing eventlet'''


@appifies(KTruth)
class truthevent(AutoActiveChainlet, TruthMixin):

    '''auto-balancing truthing eventlet'''
