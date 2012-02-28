# -*- coding: utf-8 -*-
'''active auto-balancing call chain appconf'''

from appspace import Namespace

from callchain.core.paths import Pathways

__all__ = ['autochain']


class autochain(Pathways):

    class filter(Namespace):
        collect = 'callchain.active.auto.chains.filter.collectchain'
        filter = 'callchain.active.auto.chains.filter.filterchain'
        set = 'callchain.active.auto.chains.filter.setchain'
        slice = 'callchain.active.auto.chains.filter.slicechain'

    class map(Namespace):
        copy = 'callchain.active.auto.chains.map.copychain'
        delay = 'callchain.active.auto.chains.map.delaychain'
        map = 'callchain.active.auto.chains.map.mapchain'
        repeat = 'callchain.active.auto.chains.map.repeatchain'

    class order(Namespace):
        order = 'callchain.active.auto.chains.order.orderchain'
        random = 'callchain.active.auto.chains.order.randomchain'

    class reduce(Namespace):
        math = 'callchain.active.auto.chains.reduce.mathchain'
        reduce = 'callchain.active.auto.chains.reduce.reducechain'
        truth = 'callchain.active.auto.chains.reduce.truthchain'
