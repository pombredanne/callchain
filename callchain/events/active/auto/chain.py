# -*- coding: utf-8 -*-
'''active auto-balancing event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, AutoResultMixin

from callchain.events.apps import events
from callchain.events.mixins import inside
from callchain.events.keys import KEventLink, KEventChain
from callchain.events.active.queue import EventLinkMixin, EventChainMixin

from callchain.events.active.auto.apps import event

__all__ = ['eventlink', 'eventchain']


@appifies(KEventLink)
class eventlink(EventLinkMixin, AutoQMixin):

    '''auto-balancing linked event chain'''


@appifies(KEventChain)
@inside(event, events)
class eventchain(EventChainMixin, AutoResultMixin):

    '''auto-balancing event chain'''
