# -*- coding: utf-8 -*-
'''active manually balanced event chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin, ManResultMixin

from callchain.events.apps import events
from callchain.events.mixins import inside
from callchain.events.keys import KEventLink, KEventChain
from callchain.events.active.queue import EventChainMixin, EventLinkMixin

from callchain.events.active.man.apps import event

__all__ = ['eventlink', 'eventchain']


@appifies(KEventLink)
class eventlink(EventLinkMixin, ManQMixin):

    '''manually balanced linked event chain'''


@appifies(KEventChain)
@inside(event, events)
class eventchain(EventChainMixin, ManResultMixin):

    '''manually balanced event chain'''
