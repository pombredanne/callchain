# -*- coding: utf-8 -*-
'''lazy manually balanced chains appconf'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManResultMixin, ManQMixin

from callchain.keys.root import KRoot
from callchain.keys.call import KCall
from callchain.chain import Chain, inside
from callchain.keys.core import KChainKey
from callchain.patterns import Pathways, Nameways
from callchain.services.queue import KThings, KResult


class chainbase(Pathways):
    link = 'callchain.lazy_man.chainlet.chainlink'


class chain(chainbase):

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


@appifies(KThings, KRoot, KChainKey, KCall)
@inside(chainbase)
class callchain(Chain, ManQMixin):

    ''''lazy queued manually balanced lite call chain'''


@appifies(KRoot, KChainKey, KResult, KCall)
@inside(chain)
class chainq(Chain, ManResultMixin):

    '''lazy queued manually balanced call chain'''
