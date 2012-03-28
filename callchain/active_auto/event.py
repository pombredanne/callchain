# -*- coding: utf-8 -*-
'''active auto-balancing event chains appconf'''

from appspace.keys import appifies
from twoq.active.mixins import AutoResultMixin, AutoQMixin

from callchain.keys.core import KEvent
from callchain.event import einside, Event
from callchain.keys.call import KEventCall
from callchain.keys.root import KEventRoot
from callchain.services.apps import events
from callchain.patterns import Pathways, Nameways
from callchain.services.queue import KThings, KResult


class baseevent(Pathways):
    chain = 'callchain.active_auto.chainlet.chainlink'


class event(Pathways):
    chain = 'callchain.active_auto.chainlet.chainlink'

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.active_auto.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.services.filter.KCollect'
        collect = 'callchain.active_auto.eventlet.collectevent'

    class set(Nameways):
        key = 'callchain.services.filter.KSet'
        set = 'callchain.active_auto.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.services.filter.KSlice'
        slice = 'callchain.active_auto.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.active_auto.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.services.map.KDelay'
        delay = 'callchain.active_auto.eventlet.delayevent'

    class repeat(Nameways):
        key = 'callchain.services.map.KRepeat'
        repeat = 'callchain.active_auto.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.active_auto.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.services.order.KRandom'
        random = 'callchain.active_auto.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.active_auto.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.services.reduce.KMath'
        math = 'callchain.active_auto.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.services.reduce.KTruth'
        truth = 'callchain.active_auto.eventlet.truthevent'


@appifies(KThings, KEventRoot, KEvent, KEventCall)
@einside(baseevent, events)
class eventchain(Event, AutoQMixin):

    '''active queued auto-balancing lite event chain'''


@appifies(KResult, KEventRoot, KEvent, KEventCall)
@einside(event, events)
class eventq(Event, AutoResultMixin):

    '''active queued auto-balancing event chain'''
