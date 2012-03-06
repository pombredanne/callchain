# -*- coding: utf-8 -*-
'''active auto-balancing call chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['chain']


class chain(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.keys.filter.KFilter'
        filter = 'callchain.chains.autoactive.linked.filterchain'

    class collect(Nameways):
        key = 'callchain.chains.keys.filter.KCollect'
        collect = 'callchain.chains.autoactive.linked.collectchain'

    class set(Nameways):
        key = 'callchain.chains.keys.filter.KSet'
        set = 'callchain.chains.autoactive.linked.setchain'

    class slice(Nameways):
        key = 'callchain.chains.keys.filter.KSlice'
        slice = 'callchain.chains.autoactive.linked.slicechain'

    class map(Nameways):
        key = 'callchain.chains.keys.map.KMap'
        map = 'callchain.chains.autoactive.linked.mapchain'

    class delay(Nameways):
        key = 'callchain.chains.keys.map.KDelay'
        delay = 'callchain.chains.autoactive.linked.delaychain'

    class copy(Nameways):
        key = 'callchain.chains.keys.map.KCopy'
        copy = 'callchain.chains.autoactive.linked.copychain'

    class repeat(Nameways):
        key = 'callchain.chains.keys.map.KRepeat'
        repeat = 'callchain.chains.autoactive.linked.repeatchain'

    class order(Nameways):
        key = 'callchain.chains.keys.order.KOrder'
        order = 'callchain.chains.autoactive.linked.orderchain'

    class random(Nameways):
        key = 'callchain.chains.keys.order.KRandom'
        random = 'callchain.chains.autoactive.linked.randomchain'

    class reduce(Nameways):
        key = 'callchain.chains.keys.reduce.KReduce'
        reduce = 'callchain.chains.autoactive.linked.reducechain'

    class math(Nameways):
        key = 'callchain.chains.keys.reduce.KMath'
        math = 'callchain.chains.autoactive.linked.mathchain'

    class truth(Nameways):
        key = 'callchain.chains.keys.reduce.KTruth'
        truth = 'callchain.chains.autoactive.linked.truthchain'
