# -*- coding: utf-8 -*-
'''active manually balanced call chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['manchain']


class manchain(Pathways):

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.chain.active.man.filter.filterchain'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.chain.active.man.map.mapchain'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.chain.active.man.order.orderchain'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.chain.active.man.reduce.reducechain'
