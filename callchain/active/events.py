# -*- coding: utf-8 -*-
'''callchain active event call chains'''

from stuf.utils import iterexcept

from callchain.mixins.keys import EEvent
from callchain.mixins.events import EventsQMixin, TripQMixin, EventQMixin

from callchain.active.chains import branchq, chainq


__all__ = ['eventq', 'tripq']


class eventsq(EventsQMixin):

    '''base event call chain'''

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


class tripq(eventsq, TripQMixin, branchq):

    '''trips events'''

    def _eventq(self, event):
        '''
        get call chain tied to event

        @param event: event label
        '''
        # fetch root event
        event = self._eget(event)
        # fetch branch event call chain
        queue = self.E.ez_lookup(EEvent, event)
        if queue is None:
            # create branch event call chain if nonexistent
            queue = branchq(self.M, self.M.max_length)
            self.E.ez_register(EEvent, event, queue)
        return queue


class eventq(eventsq, EventQMixin, chainq):

    '''root event chain'''

    def _eventq(self, event):
        '''
        get call chain tied to event

        @param event: event label
        '''
        # fetch event
        event = self.event(event)
        # fetch branch event call chain
        queue = self.E.ez_lookup(EEvent, event)
        if queue is None:
            # create branch event call chain if nonexistent
            queue = branchq(self)
            self.E.ez_register(EEvent, event, queue)
        return queue
