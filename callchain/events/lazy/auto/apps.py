# -*- coding: utf-8 -*-
'''lazy auto-balancing event chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.services.filter.KFilter'
        filter = 'callchain.events.lazy.auto.linked.filterevent'

    class collect(Nameways):
        key = 'callchain.chains.services.filter.KCollect'
        collect = 'callchain.events.lazy.auto.linked.collectevent'

    class set(Nameways):
        key = 'callchain.chains.services.filter.KSet'
        set = 'callchain.events.lazy.auto.linked.setevent'

    class slice(Nameways):
        key = 'callchain.chains.services.filter.KSlice'
        slice = 'callchain.events.lazy.auto.linked.sliceevent'

    class map(Nameways):
        key = 'callchain.chains.services.map.KMap'
        map = 'callchain.events.lazy.auto.linked.mapevent'

    class delay(Nameways):
        key = 'callchain.chains.services.map.KDelay'
        delay = 'callchain.events.lazy.auto.linked.delayevent'

    class copy(Nameways):
        key = 'callchain.chains.services.map.KCopy'
        copy = 'callchain.events.lazy.auto.linked.copyevent'

    class repeat(Nameways):
        key = 'callchain.chains.services.map.KRepeat'
        repeat = 'callchain.events.lazy.auto.linked.repeatevent'

    class order(Nameways):
        key = 'callchain.chains.services.order.KOrder'
        order = 'callchain.events.lazy.auto.linked.orderevent'

    class random(Nameways):
        key = 'callchain.chains.services.order.KRandom'
        random = 'callchain.events.lazy.auto.linked.randomevent'

    class reduce(Nameways):
        key = 'callchain.chains.services.reduce.KReduce'
        reduce = 'callchain.events.lazy.auto.reduce.reduceevent'

    class math(Nameways):
        key = 'callchain.chains.services.reduce.KMath'
        math = 'callchain.events.lazy.auto.linked.mathevent'

    class truth(Nameways):
        key = 'callchain.chains.services.reduce.KTruth'
        truth = 'callchain.events.lazy.auto.linked.truthevent'
