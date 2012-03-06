# -*- coding: utf-8 -*-
'''lazy auto-balancing event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin, AutoResultMixin

from callchain.chains.keys.queue import KQueue, KResults

from callchain.events.apps import events
from callchain.events.mixins import inside
from callchain.events.autolazy.apps import event
from callchain.events.keys import KEventLink, KEventChain
from callchain.events.queue import LazyChainMixin, LazyEventLinkMixin

__all__ = ('eventchain', 'eventlink')


@appifies(KEventLink, KQueue)
class eventlink(LazyEventLinkMixin, AutoQMixin):

    '''auto-balancing linked event chain'''


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(LazyChainMixin, AutoResultMixin):

    '''auto-balancing event chain'''
