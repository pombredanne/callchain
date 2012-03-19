# -*- coding: utf-8 -*-
'''active manually balanced eventlets appconf'''

from twoq.active.mixins import ManResultMixin

from callchain.internal import einside
from callchain.keys.apps import events
from callchain.chain import ActiveEventQ
from callchain.patterns import Pathways, Nameways


class event(Pathways):
    chain = 'chain.linked.chainlink'

    class filter(Nameways):
        key = 'chain.keys.filter.KFilter'
        filter = 'chain.active_man.eventlet.filterevent'

    class collect(Nameways):
        key = 'chain.keys.filter.KCollect'
        collect = 'chain.active_man.eventlet.collectevent'

    class set(Nameways):
        key = 'chain.keys.filter.KSet'
        set = 'chain.active_man.eventlet.setevent'

    class slice(Nameways):
        key = 'chain.keys.filter.KSlice'
        slice = 'chain.active_man.eventlet.sliceevent'

    class map(Nameways):
        key = 'chain.keys.map.KMap'
        map = 'chain.active_man.eventlet.mapevent'

    class delay(Nameways):
        key = 'chain.keys.map.KDelay'
        delay = 'chain.active_man.eventlet.delayevent'

    class copy(Nameways):
        key = 'chain.keys.map.KCopy'
        copy = 'chain.active_man.eventlet.copyevent'

    class repeat(Nameways):
        key = 'chain.keys.map.KRepeat'
        repeat = 'chain.active_man.eventlet.repeatevent'

    class order(Nameways):
        key = 'chain.keys.order.KOrder'
        order = 'chain.active_man.eventlet.orderevent'

    class random(Nameways):
        key = 'chain.keys.order.KRandom'
        random = 'chain.active_man.eventlet.randomevent'

    class reduce(Nameways):
        key = 'chain.keys.reduce.KReduce'
        reduce = 'chain.active_man.eventlet.reduceevent'

    class math(Nameways):
        key = 'chain.keys.reduce.KMath'
        math = 'chain.active_man.eventlet.mathevent'

    class truth(Nameways):
        key = 'chain.keys.reduce.KTruth'
        truth = 'chain.active_man.eventlet.truthevent'


@einside(event, events)
class eventq(ActiveEventQ, ManResultMixin):

    '''active queued manually balanced event chain'''
