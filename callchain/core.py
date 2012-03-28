# -*- coding: utf-8 -*-
'''callchain core'''

from appspace.keys import appifies

from callchain.managers import Events
from callchain.patterns import Pathways
from callchain.keys.core import KChain, KEvent
from callchain.keys.root import KRoot, KEventRoot
from callchain.keys.call import KCall, KEventCall
from callchain.base import ChainMixin, EventMixin
from callchain.root import RootMixin, EventRootMixin
from callchain.call import CallMixin, EventCallMixin
from callchain.branch import (
    BranchMixin, BranchletMixin, ChainletMixin, EventBranchMixin, LinkedMixin)


###############################################################################
## chain components ###########################################################
###############################################################################


class inside(object):

    '''internal chain configuration'''

    def __init__(self, pattern, required=None, defaults=None, *args, **kw):
        '''
        init

        @param pattern: pattern configuration class or appspace label
        @param required: required global settings (default: None)
        @param defaults: default global settings (default: None)
        '''
        self.pattern = pattern
        self.required = required
        self.defaults = defaults
        self.args = args
        self.kw = kw

    def __call__(self, that):
        # internal appspace manager
        that._M = Pathways.appspace(
            self.pattern,
            self.required,
            self.defaults,
            *self.args,
            **self.kw
        )
        # lock internal appspace global settings
        that._M.settings.lock()
        # set internal appspace global settings
        that._G = that._M.settings.final
        return that


@appifies(KRoot, KChain, KCall)
class Chain(CallMixin, RootMixin, ChainMixin):

    '''call chain'''


class Linked(CallMixin, BranchMixin, LinkedMixin, ChainMixin):

    '''linked chain'''


class Chainlet(ChainletMixin, BranchletMixin, BranchMixin, ChainMixin):

    '''chainlet'''


###############################################################################
## event chain components #####################################################
###############################################################################


class einside(inside):

    '''internal event chain configuration'''

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
        that = super(einside, self).__call__(that)
        that.E = Events('events')
        that.E.update(self.events)
        return that


@appifies(KEventRoot, KEvent, KEventCall)
class Event(EventCallMixin, EventRootMixin, EventMixin):

    '''event chain'''


class EventLink(EventCallMixin, EventBranchMixin, LinkedMixin, EventMixin):

    '''linked event chain'''


class Eventlet(ChainletMixin, EventBranchMixin, BranchletMixin, EventMixin):

    '''eventlet'''
