# -*- coding: utf-8 -*-
'''active manually balanced event chains appconf'''

from appspace.keys import appifies
from twoq.active.mixins import ManResultMixin, ManQMixin

from callchain.keys.core import KEvent
from callchain.event import einside, Event
from callchain.keys.call import KEventCall
from callchain.keys.root import KEventRoot
from callchain.services.apps import events
from callchain.patterns import Pathways, Nameways
from callchain.services.queue import KThings, KResult


class baseevent(Pathways):
    chain = 'callchain.active_man.chainlet.chainlink'


class event(Pathways):
    chain = 'callchain.active_man.chainlet.chainlink'

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.active_man.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.services.filter.KCollect'
        collect = 'callchain.active_man.eventlet.collectevent'

    class set(Nameways):
        key = 'callchain.services.filter.KSet'
        set = 'callchain.active_man.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.services.filter.KSlice'
        slice = 'callchain.active_man.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.active_man.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.services.map.KDelay'
        delay = 'callchain.active_man.eventlet.delayevent'

    class repeat(Nameways):
        key = 'callchain.services.map.KRepeat'
        repeat = 'callchain.active_man.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.active_man.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.services.order.KRandom'
        random = 'callchain.active_man.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.active_man.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.services.reduce.KMath'
        math = 'callchain.active_man.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.services.reduce.KTruth'
        truth = 'callchain.active_man.eventlet.truthevent'


@appifies(KThings, KEventRoot, KEvent, KEventCall)
@einside(baseevent, events)
class eventchain(Event, ManQMixin):

    '''active queued manually balanced lite event chain'''


@appifies(KResult, KEventRoot, KEvent, KEventCall)
@einside(event, events)
class eventq(Event, ManResultMixin):

    '''active queued manually balanced event chain'''
