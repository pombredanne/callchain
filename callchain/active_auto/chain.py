# -*- coding: utf-8 -*-
'''active auto-balancing chains appconf'''

from appspace import appifies
from twoq.active import AutoResultMixin

from callchain.chain import RootMixin
from callchain.config import Defaults
from callchain.keys import KRoot, KCall, KChain
from callchain.patterns import Pathways, Nameways
from callchain.services.queue import KThings, KResult
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
class callchain(RootMixin, ChainMixin, AutoResultMixin):

    '''active queued auto-balancing lite call chain'''


@appifies(KThings, KRoot, KChain, KCall)
@inside(thingchain, defaults=Defaults)
class prioritychain(RootMixin, PriorityMixin, AutoResultMixin):

    '''active priority queued auto-balancing lite call chain'''


###############################################################################
## result chain ###############################################################
###############################################################################


class chain(Pathways):
    class logger(Nameways):
        key = 'callchain.contrib.keys.KLogger'
        logger = 'callchain.contrib.logger.loglet'

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

    class combine(Nameways):
        key = 'callchain.services.order.KCombine'
        combine = 'callchain.active_auto.chainlet.combinechain'

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


@appifies(KResult, KRoot, KChain, KCall)
@inside(chain, defaults=Defaults)
class chainq(RootMixin, ChainMixin, AutoResultMixin):

    '''active queued auto-balancing call chain'''


@appifies(KThings, KRoot, KChain, KCall)
@inside(chain, defaults=Defaults)
class priorityq(RootMixin, PriorityMixin, AutoResultMixin):

    '''active priority queued auto-balancing lite call chain'''
