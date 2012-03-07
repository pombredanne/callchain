# -*- coding: utf-8 -*-
'''lazy auto-balancing event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoResultMixin

from callchain.chains.keys.queue import KResults

from callchain.events.chain import inside
from callchain.events.keys.apps import events
from callchain.events.keys.core import KEventChain
from callchain.events.chain import LazyEChainQMixin

from callchain.events.autolazy.apps import event

__all__ = ['eventchain']


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(LazyEChainQMixin, AutoResultMixin):

    '''lazy auto-balancing event chain'''
