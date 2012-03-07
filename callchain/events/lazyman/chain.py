# -*- coding: utf-8 -*-
'''lazy manually balanced event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManResultMixin

from callchain.chains.keys.queue import KResults

from callchain.events.chain import inside
from callchain.events.keys.apps import events
from callchain.events.lazyman.apps import event
from callchain.events.keys.core import KEventChain
from callchain.events.chain import LazyEChainQMixin

__all__ = ['eventchain']


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(LazyEChainQMixin, ManResultMixin):

    '''lazy manually balanced event chain'''
