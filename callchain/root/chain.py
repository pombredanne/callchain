# -*- coding: utf-8 -*-
'''root chains'''

from appspace.keys import appifies

from callchain.keys.apps import events
from callchain.mixin.fluent import ChainMixin
from callchain.internal import inside, einside
from callchain.mixin.call import ChainCallMixin
from callchain.keys.chain import KCallChain, KEventChain
from callchain.mixin.root import ChainRootMixin, EventRootMixin
from callchain.mixin.manager import ChainManagerMixin, EventManagerMixin

from callchain.root.mixins import RootMixin
from callchain.root.apps import chain, event


@appifies(KCallChain)
@inside(chain)
class callchain(
    RootMixin, ChainCallMixin, ChainManagerMixin, ChainRootMixin, ChainMixin,
):

    '''call chain'''


@appifies(KEventChain)
@einside(event, events)
class eventchain(
    RootMixin, ChainCallMixin, EventManagerMixin, EventRootMixin, ChainMixin,
):

    '''event chain'''
