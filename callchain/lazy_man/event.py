# -*- coding: utf-8 -*-
'''lazy manually balanced event chains appconf'''

from appspace import appifies
from twoq.lazy import ManResultMixin

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
    chain = 'callchain.lazy_man.chainlet.chainlink'

    class logger(Nameways):
        key = 'callchain.contrib.keys.KLogger'
        logger = 'callchain.contrib.logger.loglet'


@appifies(KThings, KEventRoot, KEvent, KEventCall)
@einside(thingevent, events, defaults=Defaults)
class eventchain(EventRootMixin, EventMixin, ManResultMixin):

    '''lazy queued manually balanced lite event chain'''


###############################################################################
## result event chain #########################################################
###############################################################################

class event(Pathways):
    chain = 'callchain.lazy_man.chainlet.chainlink'

    class logger(Nameways):
        key = 'callchain.contrib.keys.KLogger'
        logger = 'callchain.contrib.logger.loglet'

    class filter(Nameways):
        key = 'callchain.services.filter.KFilter'
        filter = 'callchain.lazy_man.eventlet.filterevent'

    class collect(Nameways):
        key = 'callchain.services.filter.KCollect'
        collect = 'callchain.lazy_man.eventlet.collectevent'

    class combine(Nameways):
        key = 'callchain.services.order.KCombine'
        combine = 'callchain.lazy_man.eventlet.combineevent'

    class set(Nameways):
        key = 'callchain.services.filter.KSet'
        set = 'callchain.lazy_man.eventlet.setevent'

    class slice(Nameways):
        key = 'callchain.services.filter.KSlice'
        slice = 'callchain.lazy_man.eventlet.sliceevent'

    class map(Nameways):
        key = 'callchain.services.map.KMap'
        map = 'callchain.lazy_man.eventlet.mapevent'

    class delay(Nameways):
        key = 'callchain.services.map.KDelay'
        delay = 'callchain.lazy_man.eventlet.delayevent'

    class repeat(Nameways):
        key = 'callchain.services.map.KRepeat'
        repeat = 'callchain.lazy_man.eventlet.repeatevent'

    class order(Nameways):
        key = 'callchain.services.order.KOrder'
        order = 'callchain.lazy_man.eventlet.orderevent'

    class random(Nameways):
        key = 'callchain.services.order.KRandom'
        random = 'callchain.lazy_man.eventlet.randomevent'

    class reduce(Nameways):
        key = 'callchain.services.reduce.KReduce'
        reduce = 'callchain.lazy_man.eventlet.reduceevent'

    class math(Nameways):
        key = 'callchain.services.reduce.KMath'
        math = 'callchain.lazy_man.eventlet.mathevent'

    class truth(Nameways):
        key = 'callchain.services.reduce.KTruth'
        truth = 'callchain.lazy_man.eventlet.truthevent'


@appifies(KResult, KEventRoot, KEvent, KEventCall)
@einside(event, events, defaults=Defaults)
class eventq(EventRootMixin, EventMixin, ManResultMixin):

    '''lazy queued manually balanced event chain'''
