# -*- coding: utf-8 -*-
'''chain assembly'''

from appspace.keys import appifies

from callchain.keys.apps import events
from callchain.apps import chain, event
from callchain.queued import QRootMixin
from callchain.internal import inside, einside
from callchain.fluent import ChainMixin, EventMixin
from callchain.root import RootMixin, EventRootMixin
from callchain.keys.chain import KCallChain, KEventChain
from callchain.call import ChainCallMixin, EventCallMixin
from callchain.manager import EventManageMixin, ManagerMixin


class Chain(ChainCallMixin, ManagerMixin, RootMixin, ChainMixin):

    '''call chain'''


class ChainQ(QRootMixin, Chain):

    '''queued call chain'''


class EventChain(EventCallMixin, EventManageMixin, EventRootMixin, EventMixin):

    '''event chain'''


class EventChainQ(QRootMixin, EventChain):

    '''queued event chain'''


@appifies(KCallChain)
@inside(chain)
class callchain(RootMixin, Chain):

    '''root call chain'''


@appifies(KEventChain)
@einside(event, events)
class eventchain(RootMixin, EventChain):

    '''root event chain'''
