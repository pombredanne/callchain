# -*- coding: utf-8 -*-
'''lazy queued call and event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoResultMixin, ManResultMixin

from callchain.services.apps import events
from callchain.services.queue import KResults
from callchain.internal import inside, einside
from callchain.assembly.chain import CallChainQ, EventChainQ

from callchain.lazy.man.apps import chain as mchain
from callchain.lazy.auto.apps import chain as achain
from callchain.lazy.man.events import event as mevent
from callchain.lazy.auto.events import event as aevent


@appifies(KResults)
@inside(achain)
class lachainq(CallChainQ, AutoResultMixin):

    '''lazy queued auto-balancing call chain'''


@appifies(KResults)
@inside(mchain)
class lmchainq(CallChainQ, ManResultMixin):

    '''lazy queued manually balanced call chain'''


@appifies(KResults)
@einside(aevent, events)
class laeventq(EventChainQ, AutoResultMixin):

    '''lazy queued auto-balancing event chain'''


@appifies(KResults)
@einside(mevent, events)
class lmeventq(EventChainQ, ManResultMixin):

    '''lazy queued manually balanced event chain'''
