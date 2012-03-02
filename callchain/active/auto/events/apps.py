# -*- coding: utf-8 -*-
'''active auto-balancing event chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['autoevent']


class autoevent(Pathways):

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        collect = 'callchain.active.auto.events.filter.collectevent'
        filter = 'callchain.active.auto.events.filter.filterevent'
        set = 'callchain.active.auto.events.filter.setevent'
        slice = 'callchain.active.auto.events.filter.sliceevent'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        copy = 'callchain.active.auto.events.map.copyevent'
        delay = 'callchain.active.auto.events.map.delayevent'
        map = 'callchain.active.auto.map.events.mapevent'
        repeat = 'callchain.active.auto.events.map.repeatevent'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.active.auto.events.order.orderevent'
        random = 'callchain.active.auto.events.order.randomevent'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        math = 'callchain.active.auto.events.reduce.mathevent'
        reduce = 'callchain.active.auto.events.reduce.reduceevent'
        truth = 'callchain.active.auto.events.reduce.truthevent'
