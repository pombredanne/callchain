# -*- coding: utf-8 -*-
'''lazy queued call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoResultMixin, ManResultMixin

from callchain.keys.apps import events
from callchain.keys.queue import KResults
from callchain.internal import inside, einside
from callchain.keys.chain import KCallChain, KEventChain
from callchain.assembly.chain import CallChainQ, EventChainQ

from callchain.lazy.man.apps import chain as mchain
from callchain.lazy.auto.apps import chain as achain
from callchain.lazy.man.events import event as mevent
from callchain.lazy.auto.events import event as aevent


@appifies(KCallChain, KResults)
@inside(achain)
class lachainq(CallChainQ, AutoResultMixin):

    '''lazy queued auto-balancing call chain'''


@appifies(KCallChain, KResults)
@inside(mchain)
class lmchainq(CallChainQ, ManResultMixin):

    '''lazy queued manually balanced call chain'''


@appifies(KEventChain, KResults)
@einside(aevent, events)
class laeventq(EventChainQ, AutoResultMixin):

    '''lazy queued auto-balancing event chain'''


@appifies(KEventChain, KResults)
@einside(mevent, events)
class lmeventq(EventChainQ, ManResultMixin):

    '''lazy queued manually balanced event chain'''
