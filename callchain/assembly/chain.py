# -*- coding: utf-8 -*-
'''chain assembly'''

from callchain.mixin.queued import QRootMixin
from callchain.mixin.fluent import ChainMixin, EventMixin
from callchain.mixin.call import ChainCallMixin, EventCallMixin
from callchain.mixin.root import ChainRootMixin, EventRootMixin
from callchain.mixin.manager import EventManagerMixin, ChainManagerMixin


class CallChain(ChainCallMixin, ChainManagerMixin, ChainRootMixin, ChainMixin):

    '''call chain'''


class CallChainQ(CallChain, QRootMixin):

    '''queued call chain'''


class EventChain(
    EventCallMixin, EventManagerMixin, EventRootMixin, EventMixin,
):

    '''event chain'''


class EventChainQ(EventChain, QRootMixin):

    '''queued event chain'''
