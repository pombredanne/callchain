# -*- coding: utf-8 -*-
'''active manually balanced call chain appconf'''

from callchain.patterns import Pathways, Nameways

__all__ = ['chain']


class chain(Pathways):
    linked = 'callchain.active.linked.amlinkq'

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.active.man.chainlet.filterchain'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.active.man.chainlet.collectchain'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.active.man.chainlet.setchain'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.active.man.chainlet.slicechain'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.active.man.chainlet.mapchain'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.active.man.chainlet.delaychain'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.active.man.chainlet.copychain'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.active.man.chainlet.repeatchain'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.active.man.chainlet.orderchain'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.active.man.chainlet.randomchain'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.active.man.chainlet.reducechain'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.active.man.chainlet.mathchain'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.active.man.chainlet.truthchain'