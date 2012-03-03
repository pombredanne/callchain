# -*- coding: utf-8 -*-
'''active manually balanced event chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['manevent']


class manevent(Pathways):

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.active.man.events.filter.filterevent'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.active.man.map.events.mapevent'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.active.man.events.order.orderevent'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.active.man.events.reduce.reduceevent'
