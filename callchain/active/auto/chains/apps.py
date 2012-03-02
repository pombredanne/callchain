# -*- coding: utf-8 -*-
'''active auto-balancing call chain appconf'''

from appspace import Namespace

from octopus import Pathways

__all__ = ['autochain']


class autochain(Pathways):

    class filter(Namespace):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.active.auto.chains.filter.filterchain'

    class map(Namespace):
        key = 'callchain.services.filter.KMap'
        map = 'callchain.active.auto.chains.map.mapchain'

    class order(Namespace):
        key = 'callchain.services.filter.KOrder'
        order = 'callchain.active.auto.chains.order.orderchain'

    class reduce(Namespace):
        key = 'callchain.services.filter.KReduce'
        reduce = 'callchain.active.auto.chains.reduce.reducechain'
