# -*- coding: utf-8 -*-
'''active man-balancing call event appconf'''

from octopus import Pathways, Nameways

__all__ = ['event']


class event(Pathways):

    class filter(Nameways):
        key = 'callevent.events.services.filter.KFilter'
        filter = 'callevent.events.active.man.filter.filterevent'

    class collect(Nameways):
        key = 'callevent.events.services.filter.KCollect'
        collect = 'callevent.events.active.man.filter.collectevent'

    class set(Nameways):
        key = 'callevent.events.services.filter.KSet'
        set = 'callevent.events.active.man.filter.setevent'

    class slice(Nameways):
        key = 'callevent.events.services.filter.KSlice'
        slice = 'callevent.events.active.man.filter.sliceevent'

    class map(Nameways):
        key = 'callevent.events.services.map.KMap'
        map = 'callevent.events.active.man.map.mapevent'

    class delay(Nameways):
        key = 'callevent.events.services.map.KDelay'
        delay = 'callevent.events.active.man.map.delayevent'

    class copy(Nameways):
        key = 'callevent.events.services.map.KCopy'
        copy = 'callevent.events.active.man.map.copyevent'

    class repeat(Nameways):
        key = 'callevent.events.services.map.KRepeat'
        repeat = 'callevent.events.active.man.map.repeatevent'

    class order(Nameways):
        key = 'callevent.events.services.order.KOrder'
        order = 'callevent.events.active.man.order.orderevent'

    class random(Nameways):
        key = 'callevent.events.services.order.KRandom'
        random = 'callevent.events.active.man.order.randomevent'

    class reduce(Nameways):
        key = 'callevent.events.services.reduce.KReduce'
        reduce = 'callevent.events.active.man.reduce.reduceevent'

    class math(Nameways):
        key = 'callevent.events.services.reduce.KMath'
        math = 'callevent.events.active.man.reduce.mathevent'

    class truth(Nameways):
        key = 'callevent.events.services.reduce.KTruth'
        truth = 'callevent.events.active.man.reduce.truthevent'
