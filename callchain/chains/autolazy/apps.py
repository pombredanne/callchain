# -*- coding: utf-8 -*-
'''lazy auto-balancing call chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['chain']


class chain(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.keys.filter.KFilter'
        filter = 'callchain.chains.autolazy.linked.filterchain'

    class collect(Nameways):
        key = 'callchain.chains.keys.filter.KCollect'
        collect = 'callchain.chains.autolazy.linked.collectchain'

    class set(Nameways):
        key = 'callchain.chains.keys.filter.KSet'
        set = 'callchain.chains.autolazy.linked.setchain'

    class slice(Nameways):
        key = 'callchain.chains.keys.filter.KSlice'
        slice = 'callchain.chains.autolazy.linked.slicechain'

    class map(Nameways):
        key = 'callchain.chains.keys.map.KMap'
        map = 'callchain.chains.autolazy.linked.mapchain'

    class delay(Nameways):
        key = 'callchain.chains.keys.map.KDelay'
        delay = 'callchain.chains.autolazy.linked.delaychain'

    class copy(Nameways):
        key = 'callchain.chains.keys.map.KCopy'
        copy = 'callchain.chains.autolazy.linked.copychain'

    class repeat(Nameways):
        key = 'callchain.chains.keys.map.KRepeat'
        repeat = 'callchain.chains.autolazy.linked.repeatchain'

    class order(Nameways):
        key = 'callchain.chains.keys.order.KOrder'
        order = 'callchain.chains.autolazy.linked.orderchain'

    class random(Nameways):
        key = 'callchain.chains.keys.order.KRandom'
        random = 'callchain.chains.autolazy.linked.randomchain'

    class reduce(Nameways):
        key = 'callchain.chains.keys.reduce.KReduce'
        reduce = 'callchain.chains.autolazy.linked.reducechain'

    class math(Nameways):
        key = 'callchain.chains.keys.reduce.KMath'
        math = 'callchain.chains.autolazy.linked.mathchain'

    class truth(Nameways):
        key = 'callchain.chains.keys.reduce.KTruth'
        truth = 'callchain.chains.autolazy.linked.truthchain'
