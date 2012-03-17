# -*- coding: utf-8 -*-
'''chain assembly'''

from callchain.mixin.queued import QRootMixin
from callchain.mixin.fluent import ChainMixin, EventMixin
from callchain.mixin.call import ChainCallMixin, EventCallMixin
from callchain.mixin.root import RootMixin, EventRootMixin
from callchain.mixin.manager import EventManageMixin, ManagerMixin


class CallChain(ChainCallMixin, ManagerMixin, RootMixin, ChainMixin):

    '''call chain'''


class CallChainQ(QRootMixin, CallChain):

    '''queued call chain'''


class EventChain(EventCallMixin, EventManageMixin, EventRootMixin, EventMixin):

    '''event chain'''


class EventChainQ(QRootMixin, EventChain):

    '''queued event chain'''
