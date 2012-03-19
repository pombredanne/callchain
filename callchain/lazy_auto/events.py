# -*- coding: utf-8 -*-
'''lazy auto-balancing eventlets appconf'''

from twoq.lazy.mixins import AutoResultMixin

from callchain.internal import einside
from callchain.keys.apps import events
from callchain.chain import EventQ
from callchain.patterns import Pathways, Nameways


class event(Pathways):
    chain = 'chain.linked.chainlink'

    class filter(Nameways):
        key = 'chain.keys.filter.KFilter'
        filter = 'chain.lazy_auto.eventlet.filterevent'

    class collect(Nameways):
        key = 'chain.keys.filter.KCollect'
        collect = 'chain.lazy_auto.eventlet.collectevent'

    class set(Nameways):
        key = 'chain.keys.filter.KSet'
        set = 'chain.lazy_auto.eventlet.setevent'

    class slice(Nameways):
        key = 'chain.keys.filter.KSlice'
        slice = 'chain.lazy_auto.eventlet.sliceevent'

    class map(Nameways):
        key = 'chain.keys.map.KMap'
        map = 'chain.lazy_auto.eventlet.mapevent'

    class delay(Nameways):
        key = 'chain.keys.map.KDelay'
        delay = 'chain.lazy_auto.eventlet.delayevent'

    class copy(Nameways):
        key = 'chain.keys.map.KCopy'
        copy = 'chain.lazy_auto.eventlet.copyevent'

    class repeat(Nameways):
        key = 'chain.keys.map.KRepeat'
        repeat = 'chain.lazy_auto.eventlet.repeatevent'

    class order(Nameways):
        key = 'chain.keys.order.KOrder'
        order = 'chain.lazy_auto.eventlet.orderevent'

    class random(Nameways):
        key = 'chain.keys.order.KRandom'
        random = 'chain.lazy_auto.eventlet.randomevent'

    class reduce(Nameways):
        key = 'chain.keys.reduce.KReduce'
        reduce = 'chain.lazy_auto.eventlet.reduceevent'

    class math(Nameways):
        key = 'chain.keys.reduce.KMath'
        math = 'chain.lazy_auto.eventlet.mathevent'

    class truth(Nameways):
        key = 'chain.keys.reduce.KTruth'
        truth = 'chain.lazy_auto.eventlet.truthevent'


@einside(event, events)
class eventq(EventQ, AutoResultMixin):

    '''lazy queued auto-balancing event chain'''
