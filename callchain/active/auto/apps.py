# -*- coding: utf-8 -*-
'''active auto-balancing call chain appconf'''

from callchain.patterns import Pathways, Nameways

__all__ = ['chain']


class chain(Pathways):
    linked = 'callchain.active.linked.aalinkq'

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.active.auto.chainlet.filterchain'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.active.auto.chainlet.collectchain'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.active.auto.chainlet.setchain'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.active.auto.chainlet.slicechain'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.active.auto.chainlet.mapchain'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.active.auto.chainlet.delaychain'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.active.auto.chainlet.copychain'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.active.auto.chainlet.repeatchain'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.active.auto.chainlet.orderchain'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.active.auto.chainlet.randomchain'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.active.auto.chainlet.reducechain'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.active.auto.chainlet.mathchain'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.active.auto.chainlet.truthchain'
