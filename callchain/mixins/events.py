# -*- coding: utf-8 -*-
'''callchain event mixins'''

from threading import local
from itertools import chain, starmap

from appspace import Registry
from twoq.support import map, items
from stuf import orderedstuf, frozenstuf

from callchain.mixins.keys import (
    EEvent, EBefore, EWork, EChange, EAfter, EProblem, EFinally, EAny)

from stuf.utils import exhaust

__all__ = ('EventQMixin', 'TripQMixin')


class EventsQMixin(local):

    '''base event call chain mixin'''

    def __init__(self):
        super(EventsQMixin, self).__init__()
        # local event registry
        self.E = Registry('events', EEvent)
        # populate system events
        ez_register = self.E.ez_register
        exhaust(starmap(
            lambda x, y: ez_register(EEvent, x, y), items(self.L.EVENTS),
        ))

    ###########################################################################
    ## event listener management ##############################################
    ###########################################################################

    def on(self, event, call, key=False, *args, **kw):
        '''
        bind callable to event

        @param event: event label
        @param call: callable or application label
        @param key: key label (default: False)
        '''
        self._eventq(event).chain(call, key, *args, **kw)
        return self

    def off(self, event):
        '''
        clear all callables bound to event

        @param event: event label
        '''
        self.E.ez_unsubscribe(EEvent, event)
        return self

    ###########################################################################
    ## event chain execution ##################################################
    ###########################################################################

    def events(self, *events):
        '''get callables bound to `*events`'''
        getit = self._getit
        return chain(*(i for i in map(getit, events)))

    def commit(self):
        '''run call chain'''
        try:
            L = self.L
            self.trigger(L.BEFORE)
            self.trigger(L.WORK)
            super(EventsQMixin, self).commit()
            self.trigger(L.CHANGE)
            self.trigger(L.ANY)
            self.trigger(L.AFTER)
        except:
            self.trigger(L.PROBLEM)
        finally:
            self.trigger(L.FINALLY)
        return self

    ###########################################################################
    ## event queue processing #################################################
    ###########################################################################

    def queues(self, *events):
        '''
        ordered mapping of per event processing queue

        @param *events: event labels
        '''
        _eventq = self._eventq
        return orderedstuf((e, _eventq(e).queue) for e in events)

    ###########################################################################
    ## events #################################################################
    ###########################################################################

    class Meta:
        ## event names ########################################################
        # 1. before events
        BEFORE = 'before',
        # 2. work events
        WORK = 'work',
        # 3. change events
        CHANGE = 'change'
        # 4. any events
        ANY = 'any'
        # 5. after event
        AFTER = 'after'
        # 6. problem event
        PROBLEM = 'problem'
        # 7. event that runs irrespective
        FINALLY = 'finally'
        ## events #############################################################
        EVENTS = frozenstuf({
            BEFORE: EBefore,
            WORK: EWork,
            CHANGE: EChange,
            ANY: EAny,
            AFTER: EAfter,
            PROBLEM: EProblem,
            FINALLY: EFinally,
        })


class TripQMixin(EventsQMixin):

    '''tripwire call chain mixin'''

    def __init__(self, root):
        '''
        init

        @param manager: manager
        '''
        super(TripQMixin, self).__init__(root)
        # root event chain getter
        self._regetit = self.root._getit
        # event getter
        self._eget = self.root.event

    ###########################################################################
    ## event chain execution ##################################################
    ###########################################################################

    def _getit(self, event):
        '''fetch callables bound to event'''
        e = self._eget(event)
        return chain(self.E.subscriptions(EEvent, e), self._regetit(e))


class EventQMixin(EventsQMixin):

    '''event call chain mixin'''

    ###########################################################################
    ## event chain execution ##################################################
    ###########################################################################

    def _getit(self, event):
        '''fetch callables bound to event'''
        return self.E.subscriptions(EEvent, self._eget(event))

    ###########################################################################
    ## event lifecycle manager ################################################
    ###########################################################################

    def event(self, event):
        '''
        create or fetch event

        @param event: event label
        '''
        self.E.key(EEvent, event)
        return self

    def unevent(self, event):
        '''
        drop event

        @param event: event label
        '''
        self.E.unkey(EEvent, event)
        return self
