# -*- coding: utf-8 -*-
'''active auto-balancing event chain appconf'''

from callchain.octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):
    linked = 'callchain.events.autoactive.linked.linkq'

    class filter(Nameways):
        key = 'callchain.chains.keys.filter.KFilter'
        filter = 'callchain.events.autoactive.chainlet.filterevent'

    class collect(Nameways):
        key = 'callchain.chains.keys.filter.KCollect'
        collect = 'callchain.events.autoactive.chainlet.collectevent'

    class set(Nameways):
        key = 'callchain.chains.keys.filter.KSet'
        set = 'callchain.events.autoactive.chainlet.setevent'

    class slice(Nameways):
        key = 'callchain.chains.keys.filter.KSlice'
        slice = 'callchain.events.autoactive.chainlet.sliceevent'

    class map(Nameways):
        key = 'callchain.chains.keys.map.KMap'
        map = 'callchain.events.autoactive.chainlet.mapevent'

    class delay(Nameways):
        key = 'callchain.chains.keys.map.KDelay'
        delay = 'callchain.events.autoactive.chainlet.delayevent'

    class copy(Nameways):
        key = 'callchain.chains.keys.map.KCopy'
        copy = 'callchain.events.autoactive.chainlet.copyevent'

    class repeat(Nameways):
        key = 'callchain.chains.keys.map.KRepeat'
        repeat = 'callchain.events.autoactive.chainlet.repeatevent'

    class order(Nameways):
        key = 'callchain.chains.keys.order.KOrder'
        order = 'callchain.events.autoactive.chainlet.orderevent'

    class random(Nameways):
        key = 'callchain.chains.keys.order.KRandom'
        random = 'callchain.events.autoactive.chainlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.chains.keys.reduce.KReduce'
        reduce = 'callchain.events.autoactive.chainlet.reduceevent'

    class math(Nameways):
        key = 'callchain.chains.keys.reduce.KMath'
        math = 'callchain.events.autoactive.chainlet.mathevent'

    class truth(Nameways):
        key = 'callchain.chains.keys.reduce.KTruth'
        truth = 'callchain.events.autoactive.chainlet.truthevent'
