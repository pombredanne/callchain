# -*- coding: utf-8 -*-
'''lazy auto-balancing event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin, AutoResultMixin

from callchain.events.apps import events
from callchain.events.mixins import inside
from callchain.events.keys import KEventLink, KEventChain
from callchain.events.lazy.mixins import EventChainMixin, EventLinkMixin

from callchain.events.lazy.man.apps import event

__all__ = ('eventchain', 'eventlink')


@appifies(KEventLink)
class eventlink(EventLinkMixin, AutoQMixin):

    '''auto-balancing linked event chain'''


@appifies(KEventChain)
@inside(event, events)
class eventchain(EventChainMixin, AutoResultMixin):

    '''auto-balancing event chain'''
