# -*- coding: utf-8 -*-
'''lazy manually balanced event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin, ManResultMixin

from callchain.chains.keys.queue import KQueue, KResults

from callchain.events.apps import events
from callchain.events.mixins import inside
from callchain.events.lazyman.apps import event
from callchain.events.keys import KEventLink, KEventChain
from callchain.events.queue import LazyEventChainMixin, LazyEventLinkMixin

__all__ = ('eventchain', 'eventlink')


@appifies(KEventLink, KQueue)
class eventlink(LazyEventLinkMixin, ManQMixin):

    '''manually balanced linked event chain'''


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(LazyEventChainMixin, ManResultMixin):

    '''manually balanced event chain'''
