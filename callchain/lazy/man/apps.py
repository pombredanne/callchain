# -*- coding: utf-8 -*-
'''lazy manually balanced call chain appconf'''

from callchain.patterns import Pathways, Nameways


class chain(Pathways):
    linked = 'callchain.lazy.linked.lmlinkq'

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.lazy.man.chainlet.filterchain'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.lazy.man.chainlet.collectchain'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.lazy.man.chainlet.setchain'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.lazy.man.chainlet.slicechain'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.lazy.man.chainlet.mapchain'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.lazy.man.chainlet.delaychain'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.lazy.man.chainlet.copychain'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.lazy.man.chainlet.repeatchain'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.lazy.man.chainlet.orderchain'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.lazy.man.chainlet.randomchain'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.lazy.man.chainlet.reducechain'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.lazy.man.chainlet.mathchain'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.lazy.man.chainlet.truthchain'
