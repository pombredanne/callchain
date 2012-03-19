# -*- coding: utf-8 -*-
'''active auto-balancing eventlets appconf'''

from appspace.keys import appifies
from twoq.active.mixins import AutoResultMixin

from callchain.chain import EventQ
from callchain.keys.apps import events
from callchain.internal import einside
from callchain.keys.queue import KResults
from callchain.patterns import Pathways, Nameways


class event(Pathways):
    chain = 'chain.linked.chainlink'

    class filter(Nameways):
        key = 'chain.keys.filter.KFilter'
        filter = 'chain.active_auto.eventlet.filterevent'

    class collect(Nameways):
        key = 'chain.keys.filter.KCollect'
        collect = 'chain.active_auto.eventlet.collectevent'

    class set(Nameways):
        key = 'chain.keys.filter.KSet'
        set = 'chain.active_auto.eventlet.setevent'

    class slice(Nameways):
        key = 'chain.keys.filter.KSlice'
        slice = 'chain.active_auto.eventlet.sliceevent'

    class map(Nameways):
        key = 'chain.keys.map.KMap'
        map = 'chain.active_auto.eventlet.mapevent'

    class delay(Nameways):
        key = 'chain.keys.map.KDelay'
        delay = 'chain.active_auto.eventlet.delayevent'

    class copy(Nameways):
        key = 'chain.keys.map.KCopy'
        copy = 'chain.active_auto.eventlet.copyevent'

    class repeat(Nameways):
        key = 'chain.keys.map.KRepeat'
        repeat = 'chain.active_auto.eventlet.repeatevent'

    class order(Nameways):
        key = 'chain.keys.order.KOrder'
        order = 'chain.active_auto.eventlet.orderevent'

    class random(Nameways):
        key = 'chain.keys.order.KRandom'
        random = 'chain.active_auto.eventlet.randomevent'

    class reduce(Nameways):
        key = 'chain.keys.reduce.KReduce'
        reduce = 'chain.active_auto.eventlet.reduceevent'

    class math(Nameways):
        key = 'chain.keys.reduce.KMath'
        math = 'chain.active_auto.eventlet.mathevent'

    class truth(Nameways):
        key = 'chain.keys.reduce.KTruth'
        truth = 'chain.active_auto.eventlet.truthevent'


@appifies(KResults)
@einside(event, events)
class eventq(EventQ, AutoResultMixin):

    '''active queued auto-balancing event chain'''
