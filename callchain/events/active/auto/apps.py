# -*- coding: utf-8 -*-
'''active auto-balancing call event appconf'''

from octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):

    class filter(Nameways):
        key = 'callevent.events.services.filter.KFilter'
        filter = 'callevent.events.active.auto.filter.filterevent'

    class collect(Nameways):
        key = 'callevent.events.services.filter.KCollect'
        collect = 'callevent.events.active.auto.filter.collectevent'

    class set(Nameways):
        key = 'callevent.events.services.filter.KSet'
        set = 'callevent.events.active.auto.filter.setevent'

    class slice(Nameways):
        key = 'callevent.events.services.filter.KSlice'
        slice = 'callevent.events.active.auto.filter.sliceevent'

    class map(Nameways):
        key = 'callevent.events.services.map.KMap'
        map = 'callevent.events.active.auto.map.mapevent'

    class delay(Nameways):
        key = 'callevent.events.services.map.KDelay'
        delay = 'callevent.events.active.auto.map.delayevent'

    class copy(Nameways):
        key = 'callevent.events.services.map.KCopy'
        copy = 'callevent.events.active.auto.map.copyevent'

    class repeat(Nameways):
        key = 'callevent.events.services.map.KRepeat'
        repeat = 'callevent.events.active.auto.map.repeatevent'

    class order(Nameways):
        key = 'callevent.events.services.order.KOrder'
        order = 'callevent.events.active.auto.order.orderevent'

    class random(Nameways):
        key = 'callevent.events.services.order.KRandom'
        random = 'callevent.events.active.auto.order.randomevent'

    class reduce(Nameways):
        key = 'callevent.events.services.reduce.KReduce'
        reduce = 'callevent.events.active.auto.reduce.reduceevent'

    class math(Nameways):
        key = 'callevent.events.services.reduce.KMath'
        math = 'callevent.events.active.auto.reduce.mathevent'

    class truth(Nameways):
        key = 'callevent.events.services.reduce.KTruth'
        truth = 'callevent.events.active.auto.reduce.truthevent'
