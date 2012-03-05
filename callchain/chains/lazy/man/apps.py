# -*- coding: utf-8 -*-
'''lazy manually balanced call chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['chain']


class chain(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.services.filter.KFilter'
        filter = 'callchain.chains.lazy.man.linked.filterchain'

    class collect(Nameways):
        key = 'callchain.chains.services.filter.KCollect'
        collect = 'callchain.chains.lazy.man.linked.collectchain'

    class set(Nameways):
        key = 'callchain.chains.services.filter.KSet'
        set = 'callchain.chains.lazy.man.linked.setchain'

    class slice(Nameways):
        key = 'callchain.chains.services.filter.KSlice'
        slice = 'callchain.chains.lazy.man.linked.slicechain'

    class map(Nameways):
        key = 'callchain.chains.services.map.KMap'
        map = 'callchain.chains.lazy.man.linked.mapchain'

    class delay(Nameways):
        key = 'callchain.chains.services.map.KDelay'
        delay = 'callchain.chains.lazy.man.linked.delaychain'

    class copy(Nameways):
        key = 'callchain.chains.services.map.KCopy'
        copy = 'callchain.chains.lazy.man.linked.copychain'

    class repeat(Nameways):
        key = 'callchain.chains.services.map.KRepeat'
        repeat = 'callchain.chains.lazy.man.linked.repeatchain'

    class order(Nameways):
        key = 'callchain.chains.services.order.KOrder'
        order = 'callchain.chains.lazy.man.linked.orderchain'

    class random(Nameways):
        key = 'callchain.chains.services.order.KRandom'
        random = 'callchain.chains.lazy.man.linked.randomchain'

    class reduce(Nameways):
        key = 'callchain.chains.services.reduce.KReduce'
        reduce = 'callchain.chains.lazy.man.reduce.reducechain'

    class math(Nameways):
        key = 'callchain.chains.services.reduce.KMath'
        math = 'callchain.chains.lazy.man.linked.mathchain'

    class truth(Nameways):
        key = 'callchain.chains.services.reduce.KTruth'
        truth = 'callchain.chains.lazy.man.linked.truthchain'
