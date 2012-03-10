# -*- coding: utf-8 -*-
'''chain assembly'''

from callchain.mixin.queued import QRootMixin
from callchain.mixin.call import CallMixin, ECallMixin, CallingMixin
from callchain.mixin.fluent import FluentMixin, ChainMixin, EventMixin
from callchain.mixin.root import RootChainMixin, RootEventMixin, RootMixin


class Chain(CallingMixin, RootMixin, FluentMixin):

    '''chain'''


class CallChain(CallMixin, RootChainMixin, ChainMixin):

    '''call chain'''


class CallChainQ(CallChain, QRootMixin):

    '''queued callchain'''


class EventChain(ECallMixin, RootEventMixin, EventMixin):

    '''event chain'''


class EventChainQ(EventChain, QRootMixin):

    '''queued event chain'''
