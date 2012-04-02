# -*- coding: utf-8 -*-
'''active manually balanced event chains appconf'''

from appspace import appifies
from twoq.active import ManResultMixin

from callchain.config import Defaults
from callchain.chain import EventRootMixin
from callchain.services.apps import events
from callchain.call import EventMixin, einside
from callchain.services import KThings, KResult
from callchain.patterns import Pathways, Nameways
from callchain.keys import KEvent, KEventRoot, KEventCall

###############################################################################
## thing event chain ##########################################################
###############################################################################


class thingevent(Pathways):
    chain = 'callchain.active_man.chainlet.chainlink'

    class logger(Nameways):
        key = 'callchain.contrib.keys.KLogger'
        logger = 'callchain.contrib.logger.loglet'


@appifies(KThings, KEventRoot, KEvent, KEventCall)
@einside(thingevent, events, defaults=Defaults)
class eventchain(EventRootMixin, EventMixin, ManResultMixin):

    '''active queued manually balanced lite event chain'''


###############################################################################
## result event chain #########################################################
###############################################################################


class event(Pathways):
    chain = 'callchain.active_man.chainlet.chainlink'

    class logger(Nameways):
        key = 'callchain.contrib.keys.KLogger'
        logger = 'callchain.contrib.logger.loglet'

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.active_man.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.services.filter.KCollect'
        collect = 'callchain.active_man.eventlet.collectevent'

    class combine(Nameways):
        key = 'callchain.services.order.KCombine'
        combine = 'callchain.active_man.eventlet.combineevent'

    class set(Nameways):
        key = 'callchain.services.filter.KSet'
        set = 'callchain.active_man.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.services.filter.KSlice'
        slice = 'callchain.active_man.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.active_man.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.services.map.KDelay'
        delay = 'callchain.active_man.eventlet.delayevent'

    class repeat(Nameways):
        key = 'callchain.services.map.KRepeat'
        repeat = 'callchain.active_man.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.active_man.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.services.order.KRandom'
        random = 'callchain.active_man.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.active_man.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.services.reduce.KMath'
        math = 'callchain.active_man.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.services.reduce.KTruth'
        truth = 'callchain.active_man.eventlet.truthevent'


@appifies(KResult, KEventRoot, KEvent, KEventCall)
@einside(event, events, defaults=Defaults)
class eventq(EventRootMixin, EventMixin, ManResultMixin):

    '''active queued manually balanced event chain'''
