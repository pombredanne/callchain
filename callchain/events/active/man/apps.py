# -*- coding: utf-8 -*-
'''active manually balanced event chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.services.filter.KFilter'
        filter = 'callchain.events.active.man.linked.filterevent'

    class collect(Nameways):
        key = 'callchain.chains.services.filter.KCollect'
        collect = 'callchain.events.active.man.linked.collectevent'

    class set(Nameways):
        key = 'callchain.chains.services.filter.KSet'
        set = 'callchain.events.active.man.linked.setevent'

    class slice(Nameways):
        key = 'callchain.chains.services.filter.KSlice'
        slice = 'callchain.events.active.man.linked.sliceevent'

    class map(Nameways):
        key = 'callchain.chains.services.map.KMap'
        map = 'callchain.events.active.man.linked.mapevent'

    class delay(Nameways):
        key = 'callchain.chains.services.map.KDelay'
        delay = 'callchain.events.active.man.linked.delayevent'

    class copy(Nameways):
        key = 'callchain.chains.services.map.KCopy'
        copy = 'callchain.events.active.man.linked.copyevent'

    class repeat(Nameways):
        key = 'callchain.chains.services.map.KRepeat'
        repeat = 'callchain.events.active.man.linked.repeatevent'

    class order(Nameways):
        key = 'callchain.chains.services.order.KOrder'
        order = 'callchain.events.active.man.linked.orderevent'

    class random(Nameways):
        key = 'callchain.chains.services.order.KRandom'
        random = 'callchain.events.active.man.linked.randomevent'

    class reduce(Nameways):
        key = 'callchain.chains.services.reduce.KReduce'
        reduce = 'callchain.events.active.man.reduce.reduceevent'

    class math(Nameways):
        key = 'callchain.chains.services.reduce.KMath'
        math = 'callchain.events.active.man.linked.mathevent'

    class truth(Nameways):
        key = 'callchain.chains.services.reduce.KTruth'
        truth = 'callchain.events.active.man.linked.truthevent'
