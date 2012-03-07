# -*- coding: utf-8 -*-
'''lazy auto-balancing event chain appconf'''

from callchain.octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):
    linked = 'callchain.events.autolazy.linked.linkq'
    callchain = 'callchain.chains.root.chain.callchain'

    class filter(Nameways):
        key = 'callchain.chains.keys.filter.KFilter'
        filter = 'callchain.events.autolazy.chainlet.filterevent'

    class collect(Nameways):
        key = 'callchain.chains.keys.filter.KCollect'
        collect = 'callchain.events.autolazy.chainlet.collectevent'

    class set(Nameways):
        key = 'callchain.chains.keys.filter.KSet'
        set = 'callchain.events.autolazy.chainlet.setevent'

    class slice(Nameways):
        key = 'callchain.chains.keys.filter.KSlice'
        slice = 'callchain.events.autolazy.chainlet.sliceevent'

    class map(Nameways):
        key = 'callchain.chains.keys.map.KMap'
        map = 'callchain.events.autolazy.chainlet.mapevent'

    class delay(Nameways):
        key = 'callchain.chains.keys.map.KDelay'
        delay = 'callchain.events.autolazy.chainlet.delayevent'

    class copy(Nameways):
        key = 'callchain.chains.keys.map.KCopy'
        copy = 'callchain.events.autolazy.chainlet.copyevent'

    class repeat(Nameways):
        key = 'callchain.chains.keys.map.KRepeat'
        repeat = 'callchain.events.autolazy.chainlet.repeatevent'

    class order(Nameways):
        key = 'callchain.chains.keys.order.KOrder'
        order = 'callchain.events.autolazy.chainlet.orderevent'

    class random(Nameways):
        key = 'callchain.chains.keys.order.KRandom'
        random = 'callchain.events.autolazy.chainlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.chains.keys.reduce.KReduce'
        reduce = 'callchain.events.autolazy.chainlet.reduceevent'

    class math(Nameways):
        key = 'callchain.chains.keys.reduce.KMath'
        math = 'callchain.events.autolazy.chainlet.mathevent'

    class truth(Nameways):
        key = 'callchain.chains.keys.reduce.KTruth'
        truth = 'callchain.events.autolazy.chainlet.truthevent'
