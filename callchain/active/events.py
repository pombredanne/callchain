# -*- coding: utf-8 -*-
'''active event chains'''

from threading import local

from stuf.utils import iterexcept

from callchain.events.services import EEvent
from callchain.events.mixins import EventLinkMixin, EventChainMixin

from callchain.active.chains import ChainLinkMixin, CallChainMixin


class _AEventMixin(local):

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
            self._sxtend(self._events(*events))
            # run event call chain until scratch queue is exhausted
            calls = iterexcept(self._scratch.popleft, IndexError)
            self.outappend(call() for call in calls)
        finally:
            # clear scratch queue
            self._sclear()
        return self

    def trigger(self, *events):
        '''add callables bound to `*events` to primary call chain'''
        self._cxtend(self._events(*events))
        return self


class LinkMixin(_AEventMixin, EventLinkMixin, ChainLinkMixin):

    '''active linked event chain mixin'''

    def _eventq(self, event):
        '''
        fetch chain tied to `event`

        @param event: event label
        '''
        # fetch event from root call chain
        event = self._eget(event)
        # fetch linked call chain bound to event
        queue = self.E.ez_lookup(EEvent, event)
        if queue is None:
            # create liked call chain if nonexistent
            queue = self._chainlink(self)
            self.E.ez_register(EEvent, event, queue)
        return queue


class ChainMixin(_AEventMixin, EventChainMixin, CallChainMixin):

    '''active event chain mixin'''

    def _eventq(self, event):
        '''
        fetch call chain tied to `event`

        @param event: event label
        '''
        # fetch event
        event = self.event(event)
        # fetch linked call chain bound to event
        queue = self.E.ez_lookup(EEvent, event)
        if queue is None:
            # create linked call chain if nonexistent
            queue = self._chainlink(self)
            self.E.ez_register(EEvent, event, queue)
        return queue
