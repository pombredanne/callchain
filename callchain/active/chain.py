# -*- coding: utf-8 -*-
'''active queued call and event chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManResultMixin, AutoResultMixin

from callchain.keys.apps import events
from callchain.keys.queue import KResults
from callchain.internal import inside, einside
from callchain.chain import ChainQ, EventChainQ

from callchain.active.mixins import ActiveContextMixin
from callchain.active.man.apps import chain as mchain
from callchain.active.auto.apps import chain as achain
from callchain.active.man.events import event as mevent
from callchain.active.auto.events import event as aevent


@appifies(KResults)
class ActiveChain(ChainQ, ActiveContextMixin):

    '''active call chain'''


@inside(achain)
class aachainq(ActiveChain, AutoResultMixin):

    '''active queued auto-balancing call chain'''


@inside(mchain)
class amchainq(ActiveChain, ManResultMixin):

    '''active queued manually balanced call chain'''


@appifies(KResults)
class ActiveEvent(EventChainQ, ActiveContextMixin):

    '''active event chain'''


@einside(aevent, events)
class aaeventq(ActiveEvent, AutoResultMixin):

    '''active queued auto-balancing event chain'''


@einside(mevent, events)
class ameventq(ActiveEvent, ManResultMixin):

    '''active queued manually balanced event chain'''
