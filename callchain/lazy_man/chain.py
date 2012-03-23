# -*- coding: utf-8 -*-
'''lazy manually balanced chains appconf'''

from appspace.keys import appifies
from twoq.active.mixins import ManMixin
from twoq.mixins.queuing import ResultMixin

from callchain.chain import ChainQ, inside
from callchain.services.queue import KQueue
from callchain.patterns import Pathways, Nameways


class callchain(Pathways):

    class finger(Nameways):
        key = 'callchain.services.queue.KFinger'
        filter = 'callchain.lazy_man.chainlet.fingerchain'

    class result(Nameways):
        key = 'callchain.services.queue.KResults'
        filter = 'callchain.lazy_man.chainlet.resultchain'

    class callable(Nameways):
        key = 'callchain.services.queue.KCallable'
        filter = 'callchain.lazy_man.chainlet.callablechain'

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.lazy_man.chainlet.filterchain'

    class collect(Nameways):
        key = 'callchain.services.filter.KCollect'
        collect = 'callchain.lazy_man.chainlet.collectchain'

    class set(Nameways):
        key = 'callchain.services.filter.KSet'
        set = 'callchain.lazy_man.chainlet.setchain'

    class slice(Nameways):
        key = 'callchain.services.filter.KSlice'
        slice = 'callchain.lazy_man.chainlet.slicechain'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.lazy_man.chainlet.mapchain'

    class delay(Nameways):
        key = 'callchain.services.map.KDelay'
        delay = 'callchain.lazy_man.chainlet.delaychain'

    class repeat(Nameways):
        key = 'callchain.services.map.KRepeat'
        repeat = 'callchain.lazy_man.chainlet.repeatchain'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.lazy_man.chainlet.orderchain'

    class random(Nameways):
        key = 'callchain.services.order.KRandom'
        random = 'callchain.lazy_man.chainlet.randomchain'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.lazy_man.chainlet.reducechain'

    class math(Nameways):
        key = 'callchain.services.reduce.KMath'
        math = 'callchain.lazy_man.chainlet.mathchain'

    class truth(Nameways):
        key = 'callchain.services.reduce.KTruth'
        truth = 'callchain.lazy_man.chainlet.truthchain'


@appifies(KQueue)
@inside(callchain)
class chainq(ChainQ, ManMixin, ResultMixin):

    '''lazy queued manually balanced call chain'''
