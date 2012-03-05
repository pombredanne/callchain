# -*- coding: utf-8 -*-
'''lazy manually balanced event chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.services.filter.KFilter'
        filter = 'callchain.events.lazy.man.linked.filterevent'

    class collect(Nameways):
        key = 'callchain.chains.services.filter.KCollect'
        collect = 'callchain.events.lazy.man.linked.collectevent'

    class set(Nameways):
        key = 'callchain.chains.services.filter.KSet'
        set = 'callchain.events.lazy.man.linked.setevent'

    class slice(Nameways):
        key = 'callchain.chains.services.filter.KSlice'
        slice = 'callchain.events.lazy.man.linked.sliceevent'

    class map(Nameways):
        key = 'callchain.chains.services.map.KMap'
        map = 'callchain.events.lazy.man.linked.mapevent'

    class delay(Nameways):
        key = 'callchain.chains.services.map.KDelay'
        delay = 'callchain.events.lazy.man.linked.delayevent'

    class copy(Nameways):
        key = 'callchain.chains.services.map.KCopy'
        copy = 'callchain.events.lazy.man.linked.copyevent'

    class repeat(Nameways):
        key = 'callchain.chains.services.map.KRepeat'
        repeat = 'callchain.events.lazy.man.linked.repeatevent'

    class order(Nameways):
        key = 'callchain.chains.services.order.KOrder'
        order = 'callchain.events.lazy.man.linked.orderevent'

    class random(Nameways):
        key = 'callchain.chains.services.order.KRandom'
        random = 'callchain.events.lazy.man.linked.randomevent'

    class reduce(Nameways):
        key = 'callchain.chains.services.reduce.KReduce'
        reduce = 'callchain.events.lazy.man.reduce.reduceevent'

    class math(Nameways):
        key = 'callchain.chains.services.reduce.KMath'
        math = 'callchain.events.lazy.man.linked.mathevent'

    class truth(Nameways):
        key = 'callchain.chains.services.reduce.KTruth'
        truth = 'callchain.events.lazy.man.linked.truthevent'
