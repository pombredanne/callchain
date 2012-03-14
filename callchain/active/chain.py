# -*- coding: utf-8 -*-
'''active queued call chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, ManQMixin

from callchain.services.apps import events
from callchain.services.queue import KResults
from callchain.internal import inside, einside
from callchain.assembly.chain import CallChainQ, EventChainQ

from callchain.active.man.apps import chain as mchain
from callchain.active.auto.apps import chain as achain
from callchain.active.man.events import event as mevent
from callchain.active.auto.events import event as aevent


@appifies(KResults)
@inside(achain)
class aachainq(CallChainQ, AutoQMixin):

    '''active queued auto-balancing call chain'''


@appifies(KResults)
@inside(mchain)
class amchainq(CallChainQ, ManQMixin):

    '''active queued manually balanced call chain'''


@appifies(KResults)
@einside(aevent, events)
class aaeventq(EventChainQ, AutoQMixin):

    '''active queued auto-balancing event chain'''


@appifies(KResults)
@einside(mevent, events)
class ameventq(EventChainQ, ManQMixin):

    '''active queued manually balanced event chain'''
