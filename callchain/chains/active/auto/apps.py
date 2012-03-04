# -*- coding: utf-8 -*-
'''active auto-balancing call chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['autochain']


class autochain(Pathways):

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.chain.active.auto.filter.filterchain'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.chain.active.auto.map.mapchain'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.chain.active.auto.order.orderchain'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.chain.active.auto.reduce.reducechain'
