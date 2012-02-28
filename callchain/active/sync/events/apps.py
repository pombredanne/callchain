# -*- coding: utf-8 -*-
'''active synchronized event chain appconf'''

from appspace import Namespace

from callchain.core.paths import Pathways

__all__ = ['syncevent']


class syncevent(Pathways):

    class filter(Namespace):
        collect = 'callchain.active.sync.events.filter.collectevent'
        filter = 'callchain.active.sync.events.filter.filterevent'
        set = 'callchain.active.sync.events.filter.setevent'
        slice = 'callchain.active.sync.events.filter.sliceevent'

    class map(Namespace):
        copy = 'callchain.active.sync.events.map.copyevent'
        delay = 'callchain.active.sync.events.map.delayevent'
        map = 'callchain.active.sync.map.events.mapevent'
        repeat = 'callchain.active.sync.events.map.repeatevent'

    class order(Namespace):
        order = 'callchain.active.sync.events.order.orderevent'
        random = 'callchain.active.sync.events.order.randomevent'

    class reduce(Namespace):
        math = 'callchain.active.sync.events.reduce.mathevent'
        reduce = 'callchain.active.sync.events.reduce.reduceevent'
        truth = 'callchain.active.sync.events.reduce.truthevent'
