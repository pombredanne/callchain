# -*- coding: utf-8 -*-
'''active queued chains'''

from appspace.keys import appifies

from callchain.keys.apps import events
from callchain.internal import inside, einside
from callchain.keys.chain import KCallChain, KEventChain

from callchain.root.apps import chain, event
from callchain.root.mixins import RootMixin
from callchain.mixin.root import RootChainMixin, RootEventMixin
from callchain.mixin.active import ActiveCallMixin, ActiveECallMixin


@appifies(KCallChain)
@inside(chain)
class callchain(RootMixin, ActiveCallMixin, RootChainMixin):

    '''call chain'''


@appifies(KEventChain)
@einside(event, events)
class eventchain(RootEventMixin, ActiveECallMixin, RootMixin):

    '''event chain'''
