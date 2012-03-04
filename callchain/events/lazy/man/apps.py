# -*- coding: utf-8 -*-
'''lazy manual balanced event chain appconf'''

from octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):

    class filter(Nameways):
        key = 'callchain.chains.services.filter.KFilter'
        filter = 'callchain.events.lazy.man.filter.filterevent'

    class collect(Nameways):
        key = 'callchain.chains.services.filter.KCollect'
        collect = 'callchain.events.lazy.man.filter.collectevent'

    class set(Nameways):
        key = 'callchain.chains.services.filter.KSet'
        set = 'callchain.events.lazy.man.filter.setevent'

    class slice(Nameways):
        key = 'callchain.chains.services.filter.KSlice'
        slice = 'callchain.events.lazy.man.filter.sliceevent'

    class map(Nameways):
        key = 'callchain.chains.services.map.KMap'
        map = 'callchain.events.lazy.man.map.mapevent'

    class delay(Nameways):
        key = 'callchain.chains.services.map.KDelay'
        delay = 'callchain.events.lazy.man.map.delayevent'

    class copy(Nameways):
        key = 'callchain.chains.services.map.KCopy'
        copy = 'callchain.events.lazy.man.map.copyevent'

    class repeat(Nameways):
        key = 'callchain.chains.services.map.KRepeat'
        repeat = 'callchain.events.lazy.man.map.repeatevent'

    class order(Nameways):
        key = 'callchain.chains.services.order.KOrder'
        order = 'callchain.events.lazy.man.order.orderevent'

    class random(Nameways):
        key = 'callchain.chains.services.order.KRandom'
        random = 'callchain.events.lazy.man.order.randomevent'

    class reduce(Nameways):
        key = 'callchain.chains.services.reduce.KReduce'
        reduce = 'callchain.events.lazy.man.reduce.reduceevent'

    class math(Nameways):
        key = 'callchain.chains.services.reduce.KMath'
        math = 'callchain.events.lazy.man.reduce.mathevent'

    class truth(Nameways):
        key = 'callchain.chains.services.reduce.KTruth'
        truth = 'callchain.events.lazy.man.reduce.truthevent'
