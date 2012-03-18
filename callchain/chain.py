# -*- coding: utf-8 -*-
'''chain assembly'''

from appspace.keys import appifies

from callchain.keys.apps import events
from callchain.apps import chain, event
from callchain.keys.queue import KResults
from callchain.internal import inside, einside
from callchain.fluent import ChainMixin, EventMixin
from callchain.keys.chain import KCallChain, KEventChain
from callchain.call import ChainCallMixin, EventCallMixin
from callchain.queued import QRootMixin, LazyContextMixin, ActiveContextMixin
from callchain.root import (
    RootMixin, EventRootMixin, EventManageMixin, ManagerMixin, CompactRootMixin)


class Chain(ChainCallMixin, ManagerMixin, RootMixin, ChainMixin):

    '''call chain'''


class ChainQ(QRootMixin, Chain):

    '''queued call chain'''


@appifies(KResults)
class ActiveChain(ChainQ, ActiveContextMixin):

    '''active call chain'''


@appifies(KResults)
class LazyChain(ChainQ, LazyContextMixin):

    '''lazy call chain'''


@appifies(KCallChain)
@inside(chain)
class callchain(CompactRootMixin, Chain):

    '''root call chain'''


class EventChain(EventCallMixin, EventManageMixin, EventRootMixin, EventMixin):

    '''event chain'''


class EventChainQ(QRootMixin, EventChain):

    '''queued event chain'''


@appifies(KResults)
class ActiveEvent(EventChainQ, ActiveContextMixin):

    '''active event chain'''


@appifies(KResults)
class LazyEvent(EventChainQ, LazyContextMixin):

    '''lazy event chain'''


@appifies(KEventChain)
@einside(event, events)
class eventchain(CompactRootMixin, EventChain):

    '''root event chain'''
