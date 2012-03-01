# -*- coding: utf-8 -*-
'''active synchronized call chain appconf'''

from appspace import Namespace

from octopus.paths import Pathways

__all__ = ['syncchain']


class syncchain(Pathways):

    class filter(Namespace):
        collect = 'callchain.active.sync.chains.filter.collectchain'
        filter = 'callchain.active.sync.chains.filter.filterchain'
        set = 'callchain.active.sync.chains.filter.setchain'
        slice = 'callchain.active.sync.chains.filter.slicechain'

    class map(Namespace):
        copy = 'callchain.active.sync.chains.map.copychain'
        delay = 'callchain.active.sync.chains.map.delaychain'
        map = 'callchain.active.sync.chains.map.mapchain'
        repeat = 'callchain.active.sync.chains.map.repeatchain'

    class order(Namespace):
        order = 'callchain.active.sync.chains.order.orderchain'
        random = 'callchain.active.sync.chains.order.randomchain'

    class reduce(Namespace):
        math = 'callchain.active.sync.chains.reduce.mathchain'
        reduce = 'callchain.active.sync.chains.reduce.reducechain'
        truth = 'callchain.active.sync.chains.reduce.truthchain'
