# -*- coding: utf-8 -*-
'''active auto-balancing event chain appconf'''

from callchain.patterns import Pathways, Nameways

__all__ = ['event']


class event(Pathways):
    linked = 'callchain.active.linked.aaeventlinkq'
    callchain = 'callchain.root.linked.chainlink'

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.active.auto.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.active.auto.eventlet.collectevent'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.active.auto.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.active.auto.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.active.auto.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.active.auto.eventlet.delayevent'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.active.auto.eventlet.copyevent'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.active.auto.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.active.auto.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.active.auto.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.active.auto.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.active.auto.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.active.auto.eventlet.truthevent'
