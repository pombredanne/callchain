# -*- coding: utf-8 -*-
'''active event chains'''

from threading import local
from inspect import ismodule

from stuf.six import items
from stuf.utils import iterexcept
from twoq.active.queuing import AutoQMixin, ManQMixin, SyncQMixin

from callchain.mixins.events.events import EEvent
from callchain.mixins.events.core import EventLinkMixin, EventChainMixin
from callchain.active.mixins import AChainLinkMixin, ACallChainMixin, ChainLink


class AEventsMixin(local):

    '''base event chain mixin'''

    ###########################################################################
    ## event chain execution ##################################################
    ###########################################################################

    def fire(self, *events):
        '''invoke callables bound to `*events` immediately'''
        try:
            # clear scratch queue
            self._sclear()
            # queue global and local bound callables
            self._sxtend(self.events(*events))
            # run event call chain until scratch queue is exhausted
            calls = iterexcept(self._scratch.popleft, IndexError)
            self.outappend(call() for call in calls)
        finally:
            # clear scratch queue
            self._sclear()
        return self

    def trigger(self, *events):
        '''add callables bound to events to primary call chain'''
        self._cxtend(self.events(*events))
        return self


class AEventLinkMixin(EventLinkMixin, AEventsMixin, AChainLinkMixin):

    '''linked event chain mixin'''

    def _eventq(self, event):
        '''
        fetch chain tied to event

        @param event: event label
        '''
        # fetch event from root call chain
        event = self._eget(event)
        # fetch linked call chain bound to event
        queue = self.E.ez_lookup(EEvent, event)
        if queue is None:
            # create liked call chain if nonexistent
            queue = ChainLink(self)
            self.E.ez_register(EEvent, event, queue)
        return queue


class AEventChainMixin(EventChainMixin, AEventsMixin, ACallChainMixin):

    '''event chain mixin'''

    def _eventq(self, event):
        '''
        fetch call chain tied to event

        @param event: event label
        '''
        # fetch event
        event = self.event(event)
        # fetch linked call chain bound to event
        queue = self.E.ez_lookup(EEvent, event)
        if queue is None:
            # create linked call chain if nonexistent
            queue = ChainLink(self)
            self.E.ez_register(EEvent, event, queue)
        return queue


###############################################################################
## active linked event chains #################################################
###############################################################################


class AEventLink(AEventLinkMixin, AutoQMixin):

    '''auto-balancing linked event chain'''

EventLink = AEventLink


class MEventLink(AEventLinkMixin, ManQMixin):

    '''manually balanced linked event chain'''


class SEventLink(AEventLinkMixin, SyncQMixin):

    '''synchronized linked event chain'''


###############################################################################
## active event chains ########################################################
###############################################################################


class AEventChain(AEventChainMixin, AutoQMixin):

    '''auto-balancing event chain'''

EventChain = AEventChain


class MEventChain(AEventChainMixin, ManQMixin):

    '''manually balanced event chain'''


class SEventChain(AEventChainMixin, SyncQMixin):

    '''synchronized event chain'''


__all__ = sorted(name for name, obj in items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
