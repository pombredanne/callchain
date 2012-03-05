# -*- coding: utf-8 -*-
'''active auto-balancing event chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.services.filter.KFilter'
        filter = 'callchain.events.active.auto.linked.filterevent'

    class collect(Nameways):
        key = 'callchain.chains.services.filter.KCollect'
        collect = 'callchain.events.active.auto.linked.collectevent'

    class set(Nameways):
        key = 'callchain.chains.services.filter.KSet'
        set = 'callchain.events.active.auto.linked.setevent'

    class slice(Nameways):
        key = 'callchain.chains.services.filter.KSlice'
        slice = 'callchain.events.active.auto.linked.sliceevent'

    class map(Nameways):
        key = 'callchain.chains.services.map.KMap'
        map = 'callchain.events.active.auto.linked.mapevent'

    class delay(Nameways):
        key = 'callchain.chains.services.map.KDelay'
        delay = 'callchain.events.active.auto.linked.delayevent'

    class copy(Nameways):
        key = 'callchain.chains.services.map.KCopy'
        copy = 'callchain.events.active.auto.linked.copyevent'

    class repeat(Nameways):
        key = 'callchain.chains.services.map.KRepeat'
        repeat = 'callchain.events.active.auto.linked.repeatevent'

    class order(Nameways):
        key = 'callchain.chains.services.order.KOrder'
        order = 'callchain.events.active.auto.linked.orderevent'

    class random(Nameways):
        key = 'callchain.chains.services.order.KRandom'
        random = 'callchain.events.active.auto.linked.randomevent'

    class reduce(Nameways):
        key = 'callchain.chains.services.reduce.KReduce'
        reduce = 'callchain.events.active.auto.reduce.reduceevent'

    class math(Nameways):
        key = 'callchain.chains.services.reduce.KMath'
        math = 'callchain.events.active.auto.linked.mathevent'

    class truth(Nameways):
        key = 'callchain.chains.services.reduce.KTruth'
        truth = 'callchain.events.active.auto.linked.truthevent'
