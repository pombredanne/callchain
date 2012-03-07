# -*- coding: utf-8 -*-
'''lazy manually balanced event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin, ManResultMixin

from callchain.chains.keys.queue import KQueue, KResults

from callchain.events.chain import inside
from callchain.events.keys.apps import events
from callchain.events.lazyman.apps import event
from callchain.events.chain import LazyEChainQMixin
from callchain.events.chainlet import LazyELetQMixin
from callchain.events.keys.core import KEventLink, KEventChain

__all__ = ('eventchain', 'eventlink')


@appifies(KEventLink, KQueue)
class eventlink(LazyELetQMixin, ManQMixin):

    '''manually balanced chainlet event chain'''


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(LazyEChainQMixin, ManResultMixin):

    '''manually balanced event chain'''
