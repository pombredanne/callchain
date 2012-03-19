# -*- coding: utf-8 -*-
'''callchain chains and events'''

from appspace.keys import appifies

from callchain.keys.apps import events
from callchain.patterns import Pathways
from callchain.internal import inside, einside
from callchain.keys.chain import KChain, KEventChain
# mixins
from callchain.queued import QRootMixin
from callchain.fluent import ChainMixin, EventMixin
from callchain.call import CallMixin, EventCallMixin
from callchain.root import (
    RootMixin, EventRootMixin, EventManageMixin, ManagerMixin, LiteMixin)

###############################################################################
## call chain #################################################################
###############################################################################


class chain(Pathways):
    link = 'callchain.link.chainlink'


class Chain(CallMixin, ManagerMixin, RootMixin, ChainMixin):

    '''call chain'''


@appifies(KChain)
@inside(chain)
class callchain(LiteMixin, Chain):

    '''root call chain'''


class ChainQ(QRootMixin, Chain):

    '''queued call chain'''

###############################################################################
## event chains ##########################################################
###############################################################################


class event(Pathways):
    event = 'callchain.linked.eventlink'
    chain = 'callchain.linked.chainlink'


class Event(EventCallMixin, EventManageMixin, EventRootMixin, EventMixin):

    '''event chain'''


@appifies(KEventChain)
@einside(event, events)
class eventchain(LiteMixin, Event):

    '''root event chain'''


class EventQ(QRootMixin, Event):

    '''queued event chain'''
