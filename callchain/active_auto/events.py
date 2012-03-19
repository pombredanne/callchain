# -*- coding: utf-8 -*-
'''active auto-balancing eventlets appconf'''

from appspace.keys import appifies
from twoq.active.mixins import AutoResultMixin

from callchain.chain import EventQ
from callchain.keys.apps import events
from callchain.internal import einside
from callchain.keys.queue import KResults
from callchain.patterns import Pathways, Nameways


class eventchain(Pathways):
    callchain = 'callchain.linked.chainlink'

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.active_auto.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.active_auto.eventlet.collectevent'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.active_auto.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.active_auto.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.active_auto.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.active_auto.eventlet.delayevent'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.active_auto.eventlet.copyevent'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.active_auto.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.active_auto.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.active_auto.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.active_auto.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.active_auto.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.active_auto.eventlet.truthevent'


@appifies(KResults)
@einside(eventchain, events)
class eventq(EventQ, AutoResultMixin):

    '''active queued auto-balancing event chain'''
