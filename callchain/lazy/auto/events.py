# -*- coding: utf-8 -*-
'''lazy auto-balancing event chain appconf'''

from callchain.patterns import Pathways, Nameways

__all__ = ['event']


class event(Pathways):
    linked = 'callchain.lazy.linked.laeventlinkq'
    callchain = 'callchain.root.linked.chainlink'

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.lazy.auto.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.lazy.auto.eventlet.collectevent'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.lazy.auto.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.lazy.auto.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.lazy.auto.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.lazy.auto.eventlet.delayevent'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.lazy.auto.eventlet.copyevent'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.lazy.auto.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.lazy.auto.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.lazy.auto.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.lazy.auto.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.lazy.auto.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.lazy.auto.eventlet.truthevent'
