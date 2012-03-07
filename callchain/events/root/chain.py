# -*- coding: utf-8 -*-
'''callchain root event chains'''

from appspace.keys import appifies

from callchain.events.keys.apps import events
from callchain.chains.keys.queue import KResults
from callchain.chains.root.chain import callchain
from callchain.events.keys.core import KEventChain
from callchain.events.chain import EChainMixin, inside

from callchain.events.root.apps import event

__all__ = ['eventchain']


@appifies(KEventChain, KResults)
@inside(event, events)
class eventchain(EChainMixin, callchain):

    '''root event chain'''
