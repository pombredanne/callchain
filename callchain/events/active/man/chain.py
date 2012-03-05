# -*- coding: utf-8 -*-
'''active manually balanced event chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin, ManResultMixin

from callchain.chains.services.queue import KQueue, KResults

from callchain.events.apps import events
from callchain.events.mixins import inside
from callchain.events.active.man.apps import event
from callchain.events.keys import KEventLink, KEventChain
from callchain.events.active.queue import EventChainMixin, EventLinkMixin

__all__ = ['eventlink', 'eventchain']


@appifies(KEventLink, KQueue)
class eventlink(EventLinkMixin, ManQMixin):

    '''manually balanced linked event chain'''


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(EventChainMixin, ManResultMixin):

    '''manually balanced event chain'''
