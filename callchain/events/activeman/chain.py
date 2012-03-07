# -*- coding: utf-8 -*-
'''active manually balanced event chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin, ManResultMixin

from callchain.chains.keys.queue import KQueue, KResults

from callchain.events.chain import inside
from callchain.events.keys.apps import events
from callchain.events.activeman.apps import event
from callchain.events.chain import ActiveEChainQMixin
from callchain.events.linked import ActiveELinkQMixin
from callchain.events.keys.core import KEventLink, KEventChain

__all__ = ['eventlink', 'eventchain']


@appifies(KEventLink, KQueue)
class eventlink(ActiveELinkQMixin, ManQMixin):

    '''manually balanced chainlet event chain'''


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(ActiveEChainQMixin, ManResultMixin):

    '''manually balanced event chain'''
