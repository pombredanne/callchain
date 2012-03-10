# -*- coding: utf-8 -*-
'''active queued chains'''

from appspace.keys import appifies

from callchain.keys.apps import events
from callchain.internal import inside, einside
from callchain.keys.chain import KCallChain, KEventChain

from callchain.root.apps import chain, event
from callchain.root.mixins import RootMixin
from callchain.mixin.root import RootChainMixin, RootEventMixin
from callchain.mixin.fluent import ChainMixin
from callchain.mixin.call import CallMixin


@appifies(KCallChain)
@inside(chain)
class callchain(RootMixin, CallMixin, RootChainMixin, ChainMixin):

    '''call chain'''


@appifies(KEventChain)
@einside(event, events)
class eventchain(RootMixin, CallMixin, RootEventMixin, ChainMixin):

    '''event chain'''
