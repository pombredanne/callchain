# -*- coding: utf-8 -*-
'''active manually balanced event chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManResultMixin

from callchain.chains.keys.queue import KResults

from callchain.events.chain import inside
from callchain.events.keys.apps import events
from callchain.events.keys.core import KEventChain
from callchain.events.chain import ActiveEChainQMixin

from callchain.events.activeman.apps import event

__all__ = ['eventchain']


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(ActiveEChainQMixin, ManResultMixin):

    '''active manually balanced event chain'''
