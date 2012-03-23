# -*- coding: utf-8 -*-
'''active manually balanced event chains appconf'''

from appspace.keys import appifies
from twoq.active.mixins import ManMixin
from twoq.mixins.queuing import ResultMixin

from callchain.services.apps import events
from callchain.event import EventQ, einside
from callchain.services.queue import KResults
from callchain.patterns import Pathways, Nameways


class event(Pathways):
    chain = 'callchain.chain.chainlink'

    class finger(Nameways):
        key = 'callchain.services.queue.KFinger'
        filter = 'callchain.active_man.chainlet.fingerevent'

    class result(Nameways):
        key = 'callchain.services.queue.KResults'
        filter = 'callchain.active_man.chainlet.resultevent'

    class callable(Nameways):
        key = 'callchain.services.queue.KCallable'
        filter = 'callchain.active_man.chainlet.callableevent'

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


@appifies(KResults)
@einside(event, events)
class eventq(EventQ, ManMixin, ResultMixin):

    '''active queued manually balanced event chain'''
