# -*- coding: utf-8 -*-
'''lazy manually balanced chainlets appconf'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManResultMixin

from callchain.chain import ChainQ
from callchain.internal import inside
from callchain.keys.queue import KResults
from callchain.patterns import Pathways, Nameways


class callchain(Pathways):

    class filter(Nameways):
        key = 'callchain.keys.filter.KFilter'
        filter = 'callchain.lazy_man.chainlet.filterchain'

    class collect(Nameways):
        key = 'callchain.keys.filter.KCollect'
        collect = 'callchain.lazy_man.chainlet.collectchain'

    class set(Nameways):
        key = 'callchain.keys.filter.KSet'
        set = 'callchain.lazy_man.chainlet.setchain'

    class slice(Nameways):
        key = 'callchain.keys.filter.KSlice'
        slice = 'callchain.lazy_man.chainlet.slicechain'

    class map(Nameways):
        key = 'callchain.keys.map.KMap'
        map = 'callchain.lazy_man.chainlet.mapchain'

    class delay(Nameways):
        key = 'callchain.keys.map.KDelay'
        delay = 'callchain.lazy_man.chainlet.delaychain'

    class copy(Nameways):
        key = 'callchain.keys.map.KCopy'
        copy = 'callchain.lazy_man.chainlet.copychain'

    class repeat(Nameways):
        key = 'callchain.keys.map.KRepeat'
        repeat = 'callchain.lazy_man.chainlet.repeatchain'

    class order(Nameways):
        key = 'callchain.keys.order.KOrder'
        order = 'callchain.lazy_man.chainlet.orderchain'

    class random(Nameways):
        key = 'callchain.keys.order.KRandom'
        random = 'callchain.lazy_man.chainlet.randomchain'

    class reduce(Nameways):
        key = 'callchain.keys.reduce.KReduce'
        reduce = 'callchain.lazy_man.chainlet.reducechain'

    class math(Nameways):
        key = 'callchain.keys.reduce.KMath'
        math = 'callchain.lazy_man.chainlet.mathchain'

    class truth(Nameways):
        key = 'callchain.keys.reduce.KTruth'
        truth = 'callchain.lazy_man.chainlet.truthchain'


@appifies(KResults)
@inside(callchain)
class chainq(ChainQ, ManResultMixin):

    '''lazy queued manually balanced call chain'''
