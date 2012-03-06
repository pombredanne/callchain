# -*- coding: utf-8 -*-
'''lazy manually balanced event chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.keys.filter.KFilter'
        filter = 'callchain.events.lazyman.linked.filterevent'

    class collect(Nameways):
        key = 'callchain.chains.keys.filter.KCollect'
        collect = 'callchain.events.lazyman.linked.collectevent'

    class set(Nameways):
        key = 'callchain.chains.keys.filter.KSet'
        set = 'callchain.events.lazyman.linked.setevent'

    class slice(Nameways):
        key = 'callchain.chains.keys.filter.KSlice'
        slice = 'callchain.events.lazyman.linked.sliceevent'

    class map(Nameways):
        key = 'callchain.chains.keys.map.KMap'
        map = 'callchain.events.lazyman.linked.mapevent'

    class delay(Nameways):
        key = 'callchain.chains.keys.map.KDelay'
        delay = 'callchain.events.lazyman.linked.delayevent'

    class copy(Nameways):
        key = 'callchain.chains.keys.map.KCopy'
        copy = 'callchain.events.lazyman.linked.copyevent'

    class repeat(Nameways):
        key = 'callchain.chains.keys.map.KRepeat'
        repeat = 'callchain.events.lazyman.linked.repeatevent'

    class order(Nameways):
        key = 'callchain.chains.keys.order.KOrder'
        order = 'callchain.events.lazyman.linked.orderevent'

    class random(Nameways):
        key = 'callchain.chains.keys.order.KRandom'
        random = 'callchain.events.lazyman.linked.randomevent'

    class reduce(Nameways):
        key = 'callchain.chains.keys.reduce.KReduce'
        reduce = 'callchain.events.lazyman.linked.reduceevent'

    class math(Nameways):
        key = 'callchain.chains.keys.reduce.KMath'
        math = 'callchain.events.lazyman.linked.mathevent'

    class truth(Nameways):
        key = 'callchain.chains.keys.reduce.KTruth'
        truth = 'callchain.events.lazyman.linked.truthevent'
