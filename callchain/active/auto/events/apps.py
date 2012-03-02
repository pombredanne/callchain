# -*- coding: utf-8 -*-
'''active auto-balancing event chain appconf'''

from appspace import Namespace

from octopus import Pathways

__all__ = ['autoevent']


class autoevent(Pathways):

    class filter(Namespace):
        key = 'callchain.services.filter.KFilter'
        collect = 'callchain.active.auto.events.filter.collectevent'
        filter = 'callchain.active.auto.events.filter.filterevent'
        set = 'callchain.active.auto.events.filter.setevent'
        slice = 'callchain.active.auto.events.filter.sliceevent'

    class map(Namespace):
        key = 'callchain.services.filter.KMap'
        copy = 'callchain.active.auto.events.map.copyevent'
        delay = 'callchain.active.auto.events.map.delayevent'
        map = 'callchain.active.auto.map.events.mapevent'
        repeat = 'callchain.active.auto.events.map.repeatevent'

    class order(Namespace):
        key = 'callchain.services.filter.KOrder'
        order = 'callchain.active.auto.events.order.orderevent'
        random = 'callchain.active.auto.events.order.randomevent'

    class reduce(Namespace):
        key = 'callchain.services.filter.KReduce'
        math = 'callchain.active.auto.events.reduce.mathevent'
        reduce = 'callchain.active.auto.events.reduce.reduceevent'
        truth = 'callchain.active.auto.events.reduce.truthevent'
