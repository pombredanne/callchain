# -*- coding: utf-8 -*-
'''lazy manually balanced event chain appconf'''

from callchain.octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):
    linked = 'callchain.events.lazyman.linked.linkq'

    class filter(Nameways):
        key = 'callchain.chains.keys.filter.KFilter'
        filter = 'callchain.events.lazyman.chainlet.filterevent'

    class collect(Nameways):
        key = 'callchain.chains.keys.filter.KCollect'
        collect = 'callchain.events.lazyman.chainlet.collectevent'

    class set(Nameways):
        key = 'callchain.chains.keys.filter.KSet'
        set = 'callchain.events.lazyman.chainlet.setevent'

    class slice(Nameways):
        key = 'callchain.chains.keys.filter.KSlice'
        slice = 'callchain.events.lazyman.chainlet.sliceevent'

    class map(Nameways):
        key = 'callchain.chains.keys.map.KMap'
        map = 'callchain.events.lazyman.chainlet.mapevent'

    class delay(Nameways):
        key = 'callchain.chains.keys.map.KDelay'
        delay = 'callchain.events.lazyman.chainlet.delayevent'

    class copy(Nameways):
        key = 'callchain.chains.keys.map.KCopy'
        copy = 'callchain.events.lazyman.chainlet.copyevent'

    class repeat(Nameways):
        key = 'callchain.chains.keys.map.KRepeat'
        repeat = 'callchain.events.lazyman.chainlet.repeatevent'

    class order(Nameways):
        key = 'callchain.chains.keys.order.KOrder'
        order = 'callchain.events.lazyman.chainlet.orderevent'

    class random(Nameways):
        key = 'callchain.chains.keys.order.KRandom'
        random = 'callchain.events.lazyman.chainlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.chains.keys.reduce.KReduce'
        reduce = 'callchain.events.lazyman.chainlet.reduceevent'

    class math(Nameways):
        key = 'callchain.chains.keys.reduce.KMath'
        math = 'callchain.events.lazyman.chainlet.mathevent'

    class truth(Nameways):
        key = 'callchain.chains.keys.reduce.KTruth'
        truth = 'callchain.events.lazyman.chainlet.truthevent'
