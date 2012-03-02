# -*- coding: utf-8 -*-
'''active manually balanced call chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['manchain']


class manchain(Pathways):

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        collect = 'callchain.active.man.chains.filter.collectchain'
        filter = 'callchain.active.man.chains.filter.filterchain'
        set = 'callchain.active.man.chains.filter.setchain'
        slice = 'callchain.active.man.chains.filter.slicechain'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        copy = 'callchain.active.man.chains.map.copychain'
        delay = 'callchain.active.man.chains.map.delaychain'
        map = 'callchain.active.man.chains.map.mapchain'
        repeat = 'callchain.active.man.chains.map.repeatchain'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.active.man.chains.order.orderchain'
        random = 'callchain.active.man.chains.order.randomchain'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        math = 'callchain.active.man.chains.reduce.mathchain'
        reduce = 'callchain.active.man.chains.reduce.reducechain'
        truth = 'callchain.active.man.chains.reduce.truthchain'
