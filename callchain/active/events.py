# -*- coding: utf-8 -*-
'''active event call chains'''

from threading import local
from inspect import ismodule

from stuf.six import items
from stuf.utils import iterexcept
from twoq.active.queuing import autoq, manq, syncq

from callchain.mixins.keys import EEvent
from callchain.mixins.events import TripQMixin, EventQMixin

from callchain.active.chains import AChainQMixin, ALinkQMixin, linkq


class AEventsQMixin(local):

    '''base event call chain mixin'''

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


class ATripQMixin(TripQMixin, AEventsQMixin, ALinkQMixin):

    '''event tripwire call chain mixin'''

    def _eventq(self, event):
        '''
        get call chain tied to tripwire

        @param event: event label
        '''
        # fetch root event
        event = self._eget(event)
        # fetch branch event call chain
        queue = self.E.ez_lookup(EEvent, event)
        if queue is None:
            # create branch event call chain if nonexistent
            queue = linkq(self.M, self.M.max_length)
            self.E.ez_register(EEvent, event, queue)
        return queue


class AEventQMixin(EventQMixin, AEventsQMixin, AChainQMixin):

    '''event call chain mixin'''

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
            queue = linkq(self)
            self.E.ez_register(EEvent, event, queue)
        return queue


###############################################################################
## active trip wire call chains ###############################################
###############################################################################


class atripq(ATripQMixin, autoq):

    '''auto-balancing tripwire call chain'''

tripq = atripq


class mtripq(ATripQMixin, manq):

    '''manually balanced tripwire call chain'''


class stripq(ATripQMixin, syncq):

    '''synchronized tripwire call chain'''


###############################################################################
## active event call chains ###################################################
###############################################################################


class aeventq(AEventQMixin, autoq):

    '''auto-balancing event call chain'''

eventq = aeventq


class meventq(AEventQMixin, manq):

    '''manually balanced event call chain'''


class seventq(AEventQMixin, syncq):

    '''synchronized event call chain'''


__all__ = sorted(name for name, obj in items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
