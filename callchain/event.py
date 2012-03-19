# -*- coding: utf-8 -*-
'''chainlink linked chains'''

from appspace.keys import appifies

from callchain.chain import inside
from callchain.managers import Events
from callchain.patterns import Pathways
from callchain.services.apps import events
from callchain.keys.events import (
    KEventChain, KEventLink, KEventLinkQ, KEventlet, KEventletQ)

from callchain.mixins.fluent import EventMixin
from callchain.mixins.call import EventCallMixin
from callchain.mixins.queued import QBranchMixin, QRootMixin
from callchain.mixins.root import EventManageMixin, EventRootMixin, LiteMixin
from callchain.mixins.branch import ChainletMixin, EventBranchMixin, LitedMixin

###############################################################################
## event chain configuration ##################################################
###############################################################################


class einside(inside):

    '''internal eventspace configuration'''

    def __init__(
        self,
        patterns=None,
        events=None,
        required=None,
        defaults=None,
        *args,
        **kw
    ):
        '''
        init

        @param patterns: pattern config or appspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(einside, self).__init__(
            patterns, required, defaults, *args, **kw
        )
        self.events = events

    def __call__(self, that):
        that = self._o_call(that)
        that.E = Events('events')
        that.E.update(self.events)
        return that

    _e_call = __call__


class event(Pathways):
    event = 'callchain.linked.eventlink'
    chain = 'callchain.linked.chainlink'

###############################################################################
## event chains ###############################################################
###############################################################################


class Event(EventCallMixin, EventManageMixin, EventRootMixin, EventMixin):

    '''event chain'''


@appifies(KEventLink)
class EventLink(EventBranchMixin, EventCallMixin, EventMixin):

    '''linked event chain'''


@appifies(KEventlet)
class Eventlet(ChainletMixin, EventBranchMixin, EventMixin):

    '''eventlet'''

###############################################################################
## linked event ###############################################################
###############################################################################


class EventQ(QRootMixin, Event):

    '''queued event chain'''


@appifies(KEventLinkQ)
class EventLinkQ(QBranchMixin, EventLink):

    '''queued linked event chain'''


@appifies(KEventletQ)
class EventletQ(QBranchMixin, Eventlet):

    '''queued eventlet'''


###############################################################################
## eventlets ##################################################################
###############################################################################


@appifies(KEventChain)
@einside(event, events)
class eventchain(LiteMixin, Event):

    '''root event chain'''


@appifies(KEventLink)
class eventlink(LitedMixin, EventLink):

    '''lite linked event chain'''


@appifies(KEventlet)
class eventlet(LitedMixin, Eventlet):

    '''root eventlet'''
