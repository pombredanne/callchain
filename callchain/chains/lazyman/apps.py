# -*- coding: utf-8 -*-
'''lazy manually balanced call chain appconf'''

from callchain.octopus import Pathways, Nameways

__all__ = ['chain']


class chain(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.keys.filter.KFilter'
        filter = 'callchain.chains.lazyman.linked.filterchain'

    class collect(Nameways):
        key = 'callchain.chains.keys.filter.KCollect'
        collect = 'callchain.chains.lazyman.linked.collectchain'

    class set(Nameways):
        key = 'callchain.chains.keys.filter.KSet'
        set = 'callchain.chains.lazyman.linked.setchain'

    class slice(Nameways):
        key = 'callchain.chains.keys.filter.KSlice'
        slice = 'callchain.chains.lazyman.linked.slicechain'

    class map(Nameways):
        key = 'callchain.chains.keys.map.KMap'
        map = 'callchain.chains.lazyman.linked.mapchain'

    class delay(Nameways):
        key = 'callchain.chains.keys.map.KDelay'
        delay = 'callchain.chains.lazyman.linked.delaychain'

    class copy(Nameways):
        key = 'callchain.chains.keys.map.KCopy'
        copy = 'callchain.chains.lazyman.linked.copychain'

    class repeat(Nameways):
        key = 'callchain.chains.keys.map.KRepeat'
        repeat = 'callchain.chains.lazyman.linked.repeatchain'

    class order(Nameways):
        key = 'callchain.chains.keys.order.KOrder'
        order = 'callchain.chains.lazyman.linked.orderchain'

    class random(Nameways):
        key = 'callchain.chains.keys.order.KRandom'
        random = 'callchain.chains.lazyman.linked.randomchain'

    class reduce(Nameways):
        key = 'callchain.chains.keys.reduce.KReduce'
        reduce = 'callchain.chains.lazyman.linked.reducechain'

    class math(Nameways):
        key = 'callchain.chains.keys.reduce.KMath'
        math = 'callchain.chains.lazyman.linked.mathchain'

    class truth(Nameways):
        key = 'callchain.chains.keys.reduce.KTruth'
        truth = 'callchain.chains.lazyman.linked.truthchain'
