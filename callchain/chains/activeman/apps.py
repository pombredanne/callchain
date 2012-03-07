# -*- coding: utf-8 -*-
'''active manually balanced call chain appconf'''

from callchain.octopus import Pathways, Nameways

__all__ = ['chain']


class chain(Pathways):
    linked = 'callchain.chains.activeman.linked.linkq'

    class filter(Nameways):
        key = 'callchain.chains.keys.filter.KFilter'
        filter = 'callchain.chains.activeman.chainlet.filterchain'

    class collect(Nameways):
        key = 'callchain.chains.keys.filter.KCollect'
        collect = 'callchain.chains.activeman.chainlet.collectchain'

    class set(Nameways):
        key = 'callchain.chains.keys.filter.KSet'
        set = 'callchain.chains.activeman.chainlet.setchain'

    class slice(Nameways):
        key = 'callchain.chains.keys.filter.KSlice'
        slice = 'callchain.chains.activeman.chainlet.slicechain'

    class map(Nameways):
        key = 'callchain.chains.keys.map.KMap'
        map = 'callchain.chains.activeman.chainlet.mapchain'

    class delay(Nameways):
        key = 'callchain.chains.keys.map.KDelay'
        delay = 'callchain.chains.activeman.chainlet.delaychain'

    class copy(Nameways):
        key = 'callchain.chains.keys.map.KCopy'
        copy = 'callchain.chains.activeman.chainlet.copychain'

    class repeat(Nameways):
        key = 'callchain.chains.keys.map.KRepeat'
        repeat = 'callchain.chains.activeman.chainlet.repeatchain'

    class order(Nameways):
        key = 'callchain.chains.keys.order.KOrder'
        order = 'callchain.chains.activeman.chainlet.orderchain'

    class random(Nameways):
        key = 'callchain.chains.keys.order.KRandom'
        random = 'callchain.chains.activeman.chainlet.randomchain'

    class reduce(Nameways):
        key = 'callchain.chains.keys.reduce.KReduce'
        reduce = 'callchain.chains.activeman.chainlet.reducechain'

    class math(Nameways):
        key = 'callchain.chains.keys.reduce.KMath'
        math = 'callchain.chains.activeman.chainlet.mathchain'

    class truth(Nameways):
        key = 'callchain.chains.keys.reduce.KTruth'
        truth = 'callchain.chains.activeman.chainlet.truthchain'
