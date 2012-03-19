# -*- coding: utf-8 -*-
'''active auto-balancing chainlets appconf'''

from appspace.keys import appifies
from twoq.active.mixins import AutoResultMixin

from callchain.chain import ChainQ
from callchain.internal import inside
from callchain.keys.queue import KResults
from callchain.patterns import Pathways, Nameways


class callchain(Pathways):

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.active_auto.chainlet.filterchain'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.active_auto.chainlet.collectchain'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.active_auto.chainlet.setchain'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.active_auto.chainlet.slicechain'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.active_auto.chainlet.mapchain'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.active_auto.chainlet.delaychain'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.active_auto.chainlet.copychain'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.active_auto.chainlet.repeatchain'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.active_auto.chainlet.orderchain'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.active_auto.chainlet.randomchain'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.active_auto.chainlet.reducechain'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.active_auto.chainlet.mathchain'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.active_auto.chainlet.truthchain'


@appifies(KResults)
@inside(callchain)
class chainq(ChainQ, AutoResultMixin):

    '''active queued auto-balancing call chain'''
