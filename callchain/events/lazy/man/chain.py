# -*- coding: utf-8 -*-
'''lazy manually balanced event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin, ManResultMixin

from callchain.events.apps import events
from callchain.events.mixins import inside
from callchain.events.keys import KEventLink, KEventChain
from callchain.events.lazy.queue import EventChainMixin, EventLinkMixin

from callchain.events.lazy.man.apps import event

__all__ = ('eventchain', 'eventlink')


@appifies(KEventLink)
class eventlink(EventLinkMixin, ManQMixin):

    '''manually balanced linked event chain'''


@appifies(KEventChain)
@inside(event, events)
class eventchain(EventChainMixin, ManResultMixin):

    '''manually balanced event chain'''
