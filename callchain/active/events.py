# -*- coding: utf-8 -*-
'''callchain active event call chains'''

from twoq import iterexcept


from callchain.mixins.events import EventsQMixin, TripQMixin, EventQMixin

from callchain.active.chains import chainsq, branchq, chainq

__all__ = ['eventq', 'tripq']


class eventsq(EventsQMixin, chainsq):

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


class eventq(eventsq, EventQMixin, chainq):

    '''root event chain'''
