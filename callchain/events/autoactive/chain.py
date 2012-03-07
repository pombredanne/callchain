# -*- coding: utf-8 -*-
'''active auto-balancing event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoResultMixin

from callchain.chains.keys.queue import KResults

from callchain.events.chain import inside
from callchain.events.keys.apps import events
from callchain.events.keys.core import KEventChain
from callchain.events.chain import ActiveEChainQMixin

from callchain.events.autoactive.apps import event

__all__ = ['eventchain']


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(ActiveEChainQMixin, AutoResultMixin):

    '''active auto-balancing event chain'''
