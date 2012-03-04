# -*- coding: utf-8 -*-
'''active auto-balancing event chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['autoevent']


class autoevent(Pathways):

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.active.auto.events.filter.filterevent'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.active.auto.map.events.mapevent'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.active.auto.events.order.orderevent'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.active.auto.events.reduce.reduceevent'
