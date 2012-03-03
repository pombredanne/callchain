# -*- coding: utf-8 -*-
'''active manually balanced call chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['manchain']


class manchain(Pathways):

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.active.man.chains.filter.filterchain'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.active.man.chains.map.mapchain'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.active.man.chains.order.orderchain'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.active.man.chains.reduce.reducechain'
