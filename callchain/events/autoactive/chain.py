# -*- coding: utf-8 -*-
'''active auto-balancing event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, AutoResultMixin

from callchain.chains.keys.queue import KQueue, KResults

from callchain.events.mixins import inside
from callchain.events.keys.apps import events
from callchain.events.autoactive.apps import event
from callchain.events.keys.core import KEventLink, KEventChain
from callchain.events.queue import ActiveEventLinkMixin, ActiveEventChainMixin

__all__ = ['eventlink', 'eventchain']


@appifies(KEventLink, KQueue)
class eventlink(ActiveEventLinkMixin, AutoQMixin):

    '''auto-balancing linked event chain'''


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(ActiveEventChainMixin, AutoResultMixin):

    '''auto-balancing event chain'''
