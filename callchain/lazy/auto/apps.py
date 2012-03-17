# -*- coding: utf-8 -*-
'''lazy auto-balancing call chainlets appconf'''

from callchain.patterns import Pathways, Nameways

__all__ = ['chain']


class chain(Pathways):
    linked = 'callchain.lazy.linked.lalinkq'

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.lazy.auto.chainlet.filterchain'

    class collect(Nameways):
        key = 'callchain.services.filter.KCollect'
        collect = 'callchain.lazy.auto.chainlet.collectchain'

    class set(Nameways):
        key = 'callchain.services.filter.KSet'
        set = 'callchain.lazy.auto.chainlet.setchain'

    class slice(Nameways):
        key = 'callchain.services.filter.KSlice'
        slice = 'callchain.lazy.auto.chainlet.slicechain'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.lazy.auto.chainlet.mapchain'

    class delay(Nameways):
        key = 'callchain.services.map.KDelay'
        delay = 'callchain.lazy.auto.chainlet.delaychain'

    class copy(Nameways):
        key = 'callchain.services.map.KCopy'
        copy = 'callchain.lazy.auto.chainlet.copychain'

    class repeat(Nameways):
        key = 'callchain.services.map.KRepeat'
        repeat = 'callchain.lazy.auto.chainlet.repeatchain'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.lazy.auto.chainlet.orderchain'

    class random(Nameways):
        key = 'callchain.services.order.KRandom'
        random = 'callchain.lazy.auto.chainlet.randomchain'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.lazy.auto.chainlet.reducechain'

    class math(Nameways):
        key = 'callchain.services.reduce.KMath'
        math = 'callchain.lazy.auto.chainlet.mathchain'

    class truth(Nameways):
        key = 'callchain.services.reduce.KTruth'
        truth = 'callchain.lazy.auto.chainlet.truthchain'
