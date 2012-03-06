# -*- coding: utf-8 -*-
'''active manually balanced call chain appconf'''

from callchain.octopus import Pathways, Nameways

__all__ = ['chain']


class chain(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.keys.filter.KFilter'
        filter = 'callchain.chains.activeman.linked.filterchain'

    class collect(Nameways):
        key = 'callchain.chains.keys.filter.KCollect'
        collect = 'callchain.chains.activeman.linked.collectchain'

    class set(Nameways):
        key = 'callchain.chains.keys.filter.KSet'
        set = 'callchain.chains.activeman.linked.setchain'

    class slice(Nameways):
        key = 'callchain.chains.keys.filter.KSlice'
        slice = 'callchain.chains.activeman.linked.slicechain'

    class map(Nameways):
        key = 'callchain.chains.keys.map.KMap'
        map = 'callchain.chains.activeman.linked.mapchain'

    class delay(Nameways):
        key = 'callchain.chains.keys.map.KDelay'
        delay = 'callchain.chains.activeman.linked.delaychain'

    class copy(Nameways):
        key = 'callchain.chains.keys.map.KCopy'
        copy = 'callchain.chains.activeman.linked.copychain'

    class repeat(Nameways):
        key = 'callchain.chains.keys.map.KRepeat'
        repeat = 'callchain.chains.activeman.linked.repeatchain'

    class order(Nameways):
        key = 'callchain.chains.keys.order.KOrder'
        order = 'callchain.chains.activeman.linked.orderchain'

    class random(Nameways):
        key = 'callchain.chains.keys.order.KRandom'
        random = 'callchain.chains.activeman.linked.randomchain'

    class reduce(Nameways):
        key = 'callchain.chains.keys.reduce.KReduce'
        reduce = 'callchain.chains.activeman.linked.reducechain'

    class math(Nameways):
        key = 'callchain.chains.keys.reduce.KMath'
        math = 'callchain.chains.activeman.linked.mathchain'

    class truth(Nameways):
        key = 'callchain.chains.keys.reduce.KTruth'
        truth = 'callchain.chains.activeman.linked.truthchain'
