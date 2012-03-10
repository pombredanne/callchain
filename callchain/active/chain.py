# -*- coding: utf-8 -*-
'''active queued call chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoResultMixin, ManResultMixin

from callchain.keys.apps import events
from callchain.keys.queue import KResults
from callchain.internal import inside, einside
from callchain.keys.chain import KCallChain, KEventChain
from callchain.assembly.chain import CallChainQ, EventChainQ

from callchain.active.man.apps import chain as mchain
from callchain.active.auto.apps import chain as achain
from callchain.active.man.events import event as mevent
from callchain.active.auto.events import event as aevent


@appifies(KCallChain, KResults)
@inside(achain)
class aachainq(CallChainQ, AutoResultMixin):

    '''active queued auto-balancing call chain'''


@appifies(KCallChain, KResults)
@inside(mchain)
class amchainq(CallChainQ, ManResultMixin):

    '''active queued manually balanced call chain'''


@appifies(KEventChain, KResults)
@einside(aevent, events)
class aaeventq(EventChainQ, AutoResultMixin):

    '''active queued auto-balancing event chain'''


@appifies(KEventChain, KResults)
@einside(mevent, events)
class ameventq(EventChainQ, ManResultMixin):

    '''active queued manually balanced event chain'''
