# -*- coding: utf-8 -*-
'''active queued chains'''

from appspace.keys import appifies

from callchain.keys.apps import events
from callchain.internal import inside, einside
from callchain.keys.chain import KCallChain, KEventChain

from callchain.root.apps import chain, event
from callchain.root.mixins import RootMixin
from callchain.mixin.root import CRootMixin, ERootMixin
from callchain.mixin.fluent import ChainMixin
from callchain.mixin.call import CCallMixin


@appifies(KCallChain)
@inside(chain)
class callchain(RootMixin, CCallMixin, CRootMixin, ChainMixin):

    '''call chain'''


@appifies(KEventChain)
@einside(event, events)
class eventchain(RootMixin, CCallMixin, ERootMixin, ChainMixin):

    '''event chain'''
