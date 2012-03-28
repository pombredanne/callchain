# -*- coding: utf-8 -*-
'''lazy manually balanced event chains appconf'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManResultMixin, ManQMixin

from callchain.keys.core import KEvent
from callchain.event import einside, Event
from callchain.keys.call import KEventCall
from callchain.keys.root import KEventRoot
from callchain.services.apps import events
from callchain.patterns import Pathways, Nameways
from callchain.services.queue import KThings, KResult


class baseevent(Pathways):
    chain = 'callchain.lazy_man.chainlet.chainlink'


class event(Pathways):
    chain = 'callchain.lazy_man.chainlet.chainlink'

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.lazy_man.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.services.filter.KCollect'
        collect = 'callchain.lazy_man.eventlet.collectevent'

    class set(Nameways):
        key = 'callchain.services.filter.KSet'
        set = 'callchain.lazy_man.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.services.filter.KSlice'
        slice = 'callchain.lazy_man.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.lazy_man.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.services.map.KDelay'
        delay = 'callchain.lazy_man.eventlet.delayevent'

    class repeat(Nameways):
        key = 'callchain.services.map.KRepeat'
        repeat = 'callchain.lazy_man.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.lazy_man.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.services.order.KRandom'
        random = 'callchain.lazy_man.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.lazy_man.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.services.reduce.KMath'
        math = 'callchain.lazy_man.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.services.reduce.KTruth'
        truth = 'callchain.lazy_man.eventlet.truthevent'


@appifies(KThings, KEventRoot, KEvent, KEventCall)
@einside(baseevent, events)
class eventchain(Event, ManQMixin):

    '''lazy queued manually balanced lite event chain'''


@appifies(KResult, KEventRoot, KEvent, KEventCall)
@einside(event, events)
class eventq(Event, ManResultMixin):

    '''lazy queued manually balanced event chain'''
