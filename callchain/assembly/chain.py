# -*- coding: utf-8 -*-
'''chain assembly'''

from callchain.mixin.queued import QRootMixin
from callchain.mixin.call import CCallMixin, ECallMixin
from callchain.mixin.fluent import ChainMixin, EventMixin
from callchain.mixin.root import CRootMixin, ERootMixin
from callchain.mixin.manager import EManagerMixin, CManagerMixin


class CallChain(CCallMixin, CManagerMixin, CRootMixin, ChainMixin):

    '''call chain'''


class CallChainQ(CallChain, QRootMixin):

    '''queued call chain'''


class EventChain(ECallMixin, EManagerMixin, ERootMixin, EventMixin):

    '''event chain'''


class EventChainQ(EventChain, QRootMixin):

    '''queued event chain'''
