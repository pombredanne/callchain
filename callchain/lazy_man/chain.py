# -*- coding: utf-8 -*-
'''lazy manually balanced chains appconf'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManResultMixin, ManQMixin

from callchain.core import inside
from callchain.root import RootMixin
from callchain.call import CallMixin
from callchain.keys.root import KRoot
from callchain.keys.call import KCall
from callchain.core import ChainMixin
from callchain.keys.core import KChain

from callchain.patterns import Pathways, Nameways
from callchain.services.queue import KThings, KResult

###############################################################################
## thing chain ################################################################
###############################################################################


class thingchain(Pathways):
    link = 'callchain.lazy_man.chainlet.chainlink'


@appifies(KThings, KRoot, KChain, KCall)
@inside(thingchain)
class callchain(CallMixin, RootMixin, ChainMixin, ManQMixin):

    ''''lazy queued manually balanced lite call chain'''


###############################################################################
## result chain ###############################################################
###############################################################################


class chain(Pathways):
    link = 'callchain.lazy_man.chainlet.chainlink'

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


@appifies(KResult, KRoot, KChain, KCall)
@inside(chain)
class chainq(CallMixin, RootMixin, ChainMixin, ManResultMixin):

    '''lazy queued manually balanced call chain'''
