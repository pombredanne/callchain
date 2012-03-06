# -*- coding: utf-8 -*-
'''active manually balanced event chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin, ManResultMixin

from callchain.chains.keys.queue import KQueue, KResults

from callchain.events.mixins import inside
from callchain.events.keys.apps import events
from callchain.events.activeman.apps import event
from callchain.events.keys.core import KEventLink, KEventChain
from callchain.events.queue import ActiveEventChainMixin, ActiveEventLinkMixin

__all__ = ['eventlink', 'eventchain']


@appifies(KEventLink, KQueue)
class eventlink(ActiveEventLinkMixin, ManQMixin):

    '''manually balanced linked event chain'''


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(ActiveEventChainMixin, ManResultMixin):

    '''manually balanced event chain'''
