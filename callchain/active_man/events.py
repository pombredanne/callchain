# -*- coding: utf-8 -*-
'''active manually balanced eventlets appconf'''

from appspace.keys import appifies
from twoq.active.mixins import ManResultMixin

from callchain.chain import EventQ
from callchain.internal import einside
from callchain.keys.apps import events
from callchain.keys.queue import KResults
from callchain.patterns import Pathways, Nameways


class eventchain(Pathways):
    callchain = 'callchain.linked.chainlink'

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.active_man.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.active_man.eventlet.collectevent'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.active_man.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.active_man.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.active_man.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.active_man.eventlet.delayevent'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.active_man.eventlet.copyevent'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.active_man.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.active_man.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.active_man.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.active_man.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.active_man.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.active_man.eventlet.truthevent'


@appifies(KResults)
@einside(eventchain, events)
class eventq(EventQ, ManResultMixin):

    '''active queued manually balanced event chain'''
