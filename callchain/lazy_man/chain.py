# -*- coding: utf-8 -*-
'''lazy manually balanced chains appconf'''

from appspace import appifies
from twoq.lazy.mixins import ManResultMixin

from callchain.chain import RootMixin
from callchain.config import Defaults
from callchain.services import KThings, KResult
from callchain.keys import KRoot, KCall, KChain
from callchain.patterns import Pathways, Nameways
from callchain.call import ChainMixin, PriorityMixin, inside

###############################################################################
## thing chain ################################################################
###############################################################################


class thingchain(Pathways):
    class logger(Nameways):
        key = 'callchain.contrib.keys.KLogger'
        logger = 'callchain.contrib.logger.loglet'


@appifies(KThings, KRoot, KChain, KCall)
@inside(thingchain, defaults=Defaults)
class callchain(RootMixin, ChainMixin, ManResultMixin):

    ''''lazy queued manually balanced lite call chain'''


@appifies(KThings, KRoot, KChain, KCall)
@inside(thingchain, defaults=Defaults)
class prioritychain(RootMixin, PriorityMixin, ManResultMixin):

    '''lazy priority queued manually balanced lite call chain'''


###############################################################################
## result chain ###############################################################
###############################################################################


class chain(Pathways):
    class logger(Nameways):
        key = 'callchain.contrib.keys.KLogger'
        logger = 'callchain.contrib.logger.loglet'

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

    class combine(Nameways):
        key = 'callchain.services.order.KCombine'
        combine = 'callchain.lazy_man.chainlet.combinechain'

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
@inside(chain, defaults=Defaults)
class chainq(RootMixin, ChainMixin, ManResultMixin):

    '''lazy queued manually balanced call chain'''


@appifies(KThings, KRoot, KChain, KCall)
@inside(chain, defaults=Defaults)
class priorityq(RootMixin, PriorityMixin, ManResultMixin):

    '''lazy priority queued manually balanced lite call chain'''
