# -*- coding: utf-8 -*-
'''active manually balanced event chain appconf'''

from appspace import Namespace

from octopus import Pathways

__all__ = ['manevent']


class manevent(Pathways):

    class filter(Namespace):
        key = 'callchain.services.filter.KFilter'
        collect = 'callchain.active.man.events.filter.collectevent'
        filter = 'callchain.active.man.events.filter.filterevent'
        set = 'callchain.active.man.events.filter.setevent'
        slice = 'callchain.active.man.events.filter.sliceevent'

    class map(Namespace):
        key = 'callchain.services.filter.KMap'
        copy = 'callchain.active.man.events.map.copyevent'
        delay = 'callchain.active.man.events.map.delayevent'
        map = 'callchain.active.man.map.events.mapevent'
        repeat = 'callchain.active.man.events.map.repeatevent'

    class order(Namespace):
        key = 'callchain.services.filter.KOrder'
        order = 'callchain.active.man.events.order.orderevent'
        random = 'callchain.active.man.events.order.randomevent'

    class reduce(Namespace):
        key = 'callchain.services.filter.KReduce'
        math = 'callchain.active.man.events.reduce.mathevent'
        reduce = 'callchain.active.man.events.reduce.reduceevent'
        truth = 'callchain.active.man.events.reduce.truthevent'
