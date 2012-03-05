# -*- coding: utf-8 -*-
'''active auto-balancing call chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['chain']


class chain(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.services.filter.KFilter'
        filter = 'callchain.chains.active.auto.linked.filterchain'

    class collect(Nameways):
        key = 'callchain.chains.services.filter.KCollect'
        collect = 'callchain.chains.active.auto.linked.collectchain'

    class set(Nameways):
        key = 'callchain.chains.services.filter.KSet'
        set = 'callchain.chains.active.auto.linked.setchain'

    class slice(Nameways):
        key = 'callchain.chains.services.filter.KSlice'
        slice = 'callchain.chains.active.auto.linked.slicechain'

    class map(Nameways):
        key = 'callchain.chains.services.map.KMap'
        map = 'callchain.chains.active.auto.linked.mapchain'

    class delay(Nameways):
        key = 'callchain.chains.services.map.KDelay'
        delay = 'callchain.chains.active.auto.linked.delaychain'

    class copy(Nameways):
        key = 'callchain.chains.services.map.KCopy'
        copy = 'callchain.chains.active.auto.linked.copychain'

    class repeat(Nameways):
        key = 'callchain.chains.services.map.KRepeat'
        repeat = 'callchain.chains.active.auto.linked.repeatchain'

    class order(Nameways):
        key = 'callchain.chains.services.order.KOrder'
        order = 'callchain.chains.active.auto.linked.orderchain'

    class random(Nameways):
        key = 'callchain.chains.services.order.KRandom'
        random = 'callchain.chains.active.auto.linked.randomchain'

    class reduce(Nameways):
        key = 'callchain.chains.services.reduce.KReduce'
        reduce = 'callchain.chains.active.auto.reduce.reducechain'

    class math(Nameways):
        key = 'callchain.chains.services.reduce.KMath'
        math = 'callchain.chains.active.auto.linked.mathchain'

    class truth(Nameways):
        key = 'callchain.chains.services.reduce.KTruth'
        truth = 'callchain.chains.active.auto.linked.truthchain'
