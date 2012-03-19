# -*- coding: utf-8 -*-
'''lazy auto-balancing eventlets appconf'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoResultMixin

from callchain.chain import EventQ
from callchain.internal import einside
from callchain.keys.apps import events
from callchain.keys.queue import KResults
from callchain.patterns import Pathways, Nameways


class event(Pathways):
    callchain = 'callchain.linked.chainlink'

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.lazy_auto.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.lazy_auto.eventlet.collectevent'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.lazy_auto.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.lazy_auto.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.lazy_auto.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.lazy_auto.eventlet.delayevent'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.lazy_auto.eventlet.copyevent'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.lazy_auto.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.lazy_auto.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.lazy_auto.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.lazy_auto.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.lazy_auto.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.lazy_auto.eventlet.truthevent'


@appifies(KResults)
@einside(event, events)
class eventq(EventQ, AutoResultMixin):

    '''lazy queued auto-balancing event chain'''
