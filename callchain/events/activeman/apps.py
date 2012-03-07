# -*- coding: utf-8 -*-
'''active manually balanced event chain appconf'''

from callchain.octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):
    linked = 'callchain.events.activeman.linked.linkq'
    callchain = 'callchain.chains.root.chain.callchain'

    class filter(Nameways):
        key = 'callchain.chains.keys.filter.KFilter'
        filter = 'callchain.events.activeman.chainlet.filterevent'

    class collect(Nameways):
        key = 'callchain.chains.keys.filter.KCollect'
        collect = 'callchain.events.activeman.chainlet.collectevent'

    class set(Nameways):
        key = 'callchain.chains.keys.filter.KSet'
        set = 'callchain.events.activeman.chainlet.setevent'

    class slice(Nameways):
        key = 'callchain.chains.keys.filter.KSlice'
        slice = 'callchain.events.activeman.chainlet.sliceevent'

    class map(Nameways):
        key = 'callchain.chains.keys.map.KMap'
        map = 'callchain.events.activeman.chainlet.mapevent'

    class delay(Nameways):
        key = 'callchain.chains.keys.map.KDelay'
        delay = 'callchain.events.activeman.chainlet.delayevent'

    class copy(Nameways):
        key = 'callchain.chains.keys.map.KCopy'
        copy = 'callchain.events.activeman.chainlet.copyevent'

    class repeat(Nameways):
        key = 'callchain.chains.keys.map.KRepeat'
        repeat = 'callchain.events.activeman.chainlet.repeatevent'

    class order(Nameways):
        key = 'callchain.chains.keys.order.KOrder'
        order = 'callchain.events.activeman.chainlet.orderevent'

    class random(Nameways):
        key = 'callchain.chains.keys.order.KRandom'
        random = 'callchain.events.activeman.chainlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.chains.keys.reduce.KReduce'
        reduce = 'callchain.events.activeman.chainlet.reduceevent'

    class math(Nameways):
        key = 'callchain.chains.keys.reduce.KMath'
        math = 'callchain.events.activeman.chainlet.mathevent'

    class truth(Nameways):
        key = 'callchain.chains.keys.reduce.KTruth'
        truth = 'callchain.events.activeman.chainlet.truthevent'
