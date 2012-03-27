# -*- coding: utf-8 -*-
'''active auto-balancing chains appconf'''

from appspace.keys import appifies
from twoq.active.mixins import AutoResultMixin, AutoQMixin

from callchain.keys.root import KRoot
from callchain.keys.call import KCall
from callchain.chain import Chain, inside
from callchain.keys.core import KChainKey
from callchain.patterns import Pathways, Nameways
from callchain.services.queue import KThings, KResult


class chainbase(Pathways):
    link = 'callchain.active_auto.chainlet.chainlink'


class chain(chainbase):

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.active_auto.chainlet.filterchain'

    class collect(Nameways):
        key = 'callchain.services.filter.KCollect'
        collect = 'callchain.active_auto.chainlet.collectchain'

    class set(Nameways):
        key = 'callchain.services.filter.KSet'
        set = 'callchain.active_auto.chainlet.setchain'

    class slice(Nameways):
        key = 'callchain.services.filter.KSlice'
        slice = 'callchain.active_auto.chainlet.slicechain'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.active_auto.chainlet.mapchain'

    class delay(Nameways):
        key = 'callchain.services.map.KDelay'
        delay = 'callchain.active_auto.chainlet.delaychain'

    class repeat(Nameways):
        key = 'callchain.services.map.KRepeat'
        repeat = 'callchain.active_auto.chainlet.repeatchain'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.active_auto.chainlet.orderchain'

    class random(Nameways):
        key = 'callchain.services.order.KRandom'
        random = 'callchain.active_auto.chainlet.randomchain'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.active_auto.chainlet.reducechain'

    class math(Nameways):
        key = 'callchain.services.reduce.KMath'
        math = 'callchain.active_auto.chainlet.mathchain'

    class truth(Nameways):
        key = 'callchain.services.reduce.KTruth'
        truth = 'callchain.active_auto.chainlet.truthchain'


@appifies(KThings, KRoot, KChainKey, KCall)
@inside(chainbase)
class callchain(Chain, AutoQMixin):

    '''active queued auto-balancing lite call chain'''


@appifies(KRoot, KChainKey, KResult, KCall)
@inside(chain)
class chainq(Chain, AutoResultMixin):

    '''active queued auto-balancing call chain'''
