# -*- coding: utf-8 -*-
'''chain chains'''

from appspace.keys import appifies

from callchain.keys.apps import events
from callchain.apps import chain, event
from callchain.queued import QRootMixin
from callchain.internal import inside, einside
from callchain.fluent import ChainMixin, EventMixin
from callchain.keys.chain import KChain, KEventChain
from callchain.call import CallMixin, EventCallMixin
from callchain.root import (
    RootMixin, EventRootMixin, EventManageMixin, ManagerMixin, SingleMixin)

###############################################################################
## chains #####################################################################
###############################################################################


class Chain(CallMixin, ManagerMixin, RootMixin, ChainMixin):

    '''call chain'''


@appifies(KChain)
@inside(chain)
class chain(SingleMixin, Chain):

    '''root call chain'''


class ChainQ(QRootMixin, Chain):

    '''queued call chain'''


###############################################################################
## event chains ###############################################################
###############################################################################


class Event(EventCallMixin, EventManageMixin, EventRootMixin, EventMixin):

    '''event chain'''


@appifies(KEventChain)
@einside(event, events)
class event(SingleMixin, Event):

    '''root event chain'''


class EventQ(QRootMixin, Event):

    '''queued event chain'''
