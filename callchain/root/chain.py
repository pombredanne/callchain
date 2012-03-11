# -*- coding: utf-8 -*-
'''active queued chains'''

from appspace.keys import appifies

from callchain.keys.apps import events
from callchain.mixin.call import CCallMixin
from callchain.mixin.fluent import ChainMixin
from callchain.internal import inside, einside
from callchain.mixin.root import CRootMixin, ERootMixin
from callchain.keys.chain import KCallChain, KEventChain
from callchain.mixin.manager import CManagerMixin, EManagerMixin

from callchain.root.apps import chain, event
from callchain.root.mixins import RootMixin


@appifies(KCallChain)
@inside(chain)
class callchain(RootMixin, CCallMixin, CManagerMixin, CRootMixin, ChainMixin):

    '''call chain'''


@appifies(KEventChain)
@einside(event, events)
class eventchain(RootMixin, CCallMixin, EManagerMixin, ERootMixin, ChainMixin):

    '''event chain'''
