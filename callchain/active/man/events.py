# -*- coding: utf-8 -*-
'''active manually balanced event chain appconf'''

from callchain.patterns import Pathways, Nameways

__all__ = ['event']


class event(Pathways):
    linked = 'callchain.active.linked.ameventlinkq'
    callchain = 'callchain.root.linked.chainlink'

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.active.man.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.active.man.eventlet.collectevent'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.active.man.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.active.man.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.active.man.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.active.man.eventlet.delayevent'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.active.man.eventlet.copyevent'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.active.man.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.active.man.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.active.man.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.active.man.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.active.man.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.active.man.eventlet.truthevent'
