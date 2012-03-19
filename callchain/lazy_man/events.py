# -*- coding: utf-8 -*-
'''lazy manually balanced eventlets appconf'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManResultMixin

from callchain.chain import EventQ
from callchain.internal import einside
from callchain.keys.apps import events
from callchain.keys.queue import KResults
from callchain.patterns import Pathways, Nameways


class event(Pathways):
    chain = 'chain.linked.chainlink'

    class filter(Nameways):
        key = 'chain.keys.filter.KFilter'
        filter = 'chain.lazy_man.eventlet.filterevent'

    class collect(Nameways):
        key = 'chain.keys.filter.KCollect'
        collect = 'chain.lazy_man.eventlet.collectevent'

    class set(Nameways):
        key = 'chain.keys.filter.KSet'
        set = 'chain.lazy_man.eventlet.setevent'

    class slice(Nameways):
        key = 'chain.keys.filter.KSlice'
        slice = 'chain.lazy_man.eventlet.sliceevent'

    class map(Nameways):
        key = 'chain.keys.map.KMap'
        map = 'chain.lazy_man.eventlet.mapevent'

    class delay(Nameways):
        key = 'chain.keys.map.KDelay'
        delay = 'chain.lazy_man.eventlet.delayevent'

    class copy(Nameways):
        key = 'chain.keys.map.KCopy'
        copy = 'chain.lazy_man.eventlet.copyevent'

    class repeat(Nameways):
        key = 'chain.keys.map.KRepeat'
        repeat = 'chain.lazy_man.eventlet.repeatevent'

    class order(Nameways):
        key = 'chain.keys.order.KOrder'
        order = 'chain.lazy_man.eventlet.orderevent'

    class random(Nameways):
        key = 'chain.keys.order.KRandom'
        random = 'chain.lazy_man.eventlet.randomevent'

    class reduce(Nameways):
        key = 'chain.keys.reduce.KReduce'
        reduce = 'chain.lazy_man.eventlet.reduceevent'

    class math(Nameways):
        key = 'chain.keys.reduce.KMath'
        math = 'chain.lazy_man.eventlet.mathevent'

    class truth(Nameways):
        key = 'chain.keys.reduce.KTruth'
        truth = 'chain.lazy_man.eventlet.truthevent'


@appifies(KResults)
@einside(event, events)
class eventq(EventQ, ManResultMixin):

    '''lazy queued manually balanced event chain'''
