# -*- coding: utf-8 -*-
'''lazy auto-balancing event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin, AutoResultMixin

from callchain.chains.keys.queue import KQueue, KResults

from callchain.events.core import inside
from callchain.events.keys.apps import events
from callchain.events.autolazy.apps import event
from callchain.events.keys.core import KEventLink, KEventChain
from callchain.events.linked import LazyELinkQMixin
from callchain.events.chain import LazyEChainQMixin

__all__ = ('eventchain', 'eventlink')


@appifies(KEventLink, KQueue)
class eventlink(LazyELinkQMixin, AutoQMixin):

    '''auto-balancing linked event chain'''


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(LazyEChainQMixin, AutoResultMixin):

    '''auto-balancing event chain'''
