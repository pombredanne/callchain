# -*- coding: utf-8 -*-
'''active manually balanced chains appconf'''

from appspace.keys import appifies
from twoq.active.mixins import ManMixin
from twoq.mixins.queuing import ResultMixin

from callchain.chain import ChainQ, inside
from callchain.services.queue import KQueue
from callchain.patterns import Pathways, Nameways


class callchain(Pathways):

    class finger(Nameways):
        key = 'callchain.services.queue.KFinger'
        filter = 'callchain.active_man.chainlet.fingerchain'

    class result(Nameways):
        key = 'callchain.services.queue.KResults'
        filter = 'callchain.active_man.chainlet.resultchain'

    class callable(Nameways):
        key = 'callchain.services.queue.KCallable'
        filter = 'callchain.active_man.chainlet.callablechain'

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.active_man.chainlet.filterchain'

    class collect(Nameways):
        key = 'callchain.services.filter.KCollect'
        collect = 'callchain.active_man.chainlet.collectchain'

    class set(Nameways):
        key = 'callchain.services.filter.KSet'
        set = 'callchain.active_man.chainlet.setchain'

    class slice(Nameways):
        key = 'callchain.services.filter.KSlice'
        slice = 'callchain.active_man.chainlet.slicechain'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.active_man.chainlet.mapchain'

    class delay(Nameways):
        key = 'callchain.services.map.KDelay'
        delay = 'callchain.active_man.chainlet.delaychain'

    class repeat(Nameways):
        key = 'callchain.services.map.KRepeat'
        repeat = 'callchain.active_man.chainlet.repeatchain'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.active_man.chainlet.orderchain'

    class random(Nameways):
        key = 'callchain.services.order.KRandom'
        random = 'callchain.active_man.chainlet.randomchain'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.active_man.chainlet.reducechain'

    class math(Nameways):
        key = 'callchain.services.reduce.KMath'
        math = 'callchain.active_man.chainlet.mathchain'

    class truth(Nameways):
        key = 'callchain.services.reduce.KTruth'
        truth = 'callchain.active_man.chainlet.truthchain'


@appifies(KQueue)
@inside(callchain)
class chainq(ChainQ, ManMixin, ResultMixin):

    '''active queued manually balanced call chain'''
