# -*- coding: utf-8 -*-
'''event chain mixins'''

from itertools import chain, starmap

from appspace import Registry
from stuf.utils import exhaust
from twoq.support import map, items
from octopus import Tentacle, Octopus
from stuf import orderedstuf, frozenstuf
from octopus.resets import ResetLocalMixin

from callchain.events.services import (
    EEvent, EBefore, EWork, EChange, EAfter, EProblem, EFinally, EAny)

__all__ = ('EventChainMixin', 'EventLinkMixin')


class _EventMixin(ResetLocalMixin):

    '''base event chain mixin'''

    def __init__(self):
        super(_EventMixin, self).__init__()
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

    def _events(self, *events):
        '''get callables bound to `*events`'''
        getit = self._getevent
        return chain(*(i for i in map(getit, events)))

    def commit(self):
        '''run event chain'''
        try:
            L = self.L
            self.trigger(L.BEFORE)
            self.trigger(L.WORK)
            super(_EventMixin, self).commit()
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

    def events(self, *events):
        '''
        ordered mapping of each event processing queue

        @param *events: event labels
        '''
        _eventq = self._eventq
        return orderedstuf((e, _eventq(e).queue) for e in events)

    ###########################################################################
    ## events #################################################################
    ###########################################################################

    class Meta:
        ## event names ########################################################
        # 1. before event
        BEFORE = 'before'
        # 2. work event
        WORK = 'work'
        # 3. change event
        CHANGE = 'change'
        # 4. any event
        ANY = 'any'
        # 5. after event
        AFTER = 'after'
        # 6. problem event
        PROBLEM = 'problem'
        # 7. event that runs irrespective
        FINALLY = 'anyway'
        ## events #############################################################
        EVENTS = frozenstuf({
            # 1. before event
            BEFORE: EBefore,
            # 2. work event
            WORK: EWork,
            # 3. change event
            CHANGE: EChange,
            # 4. any event
            ANY: EAny,
            # 5. after event
            AFTER: EAfter,
            # 6. problem event
            PROBLEM: EProblem,
            # 7. event that runs irrespective
            FINALLY: EFinally,
        })



class EventChainMixin(_EventMixin, Octopus):

    '''base event chain mixin'''

    def _getevent(self, event):
        '''fetch callables bound to event'''
        return self.E.subscriptions(EEvent, self._eget(event))

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
    

class EventLinkMixin(_EventMixin, Tentacle):

    '''base linked event chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root event chain
        '''
        super(EventLinkMixin, self).__init__(root)
        # root event chain getter
        self._regetit = self.root._getevent
        # event getter
        self._eget = self.root.event

    def _getevent(self, event):
        '''fetch callables bound to event'''
        e = self._eget(event)
        return chain(self.E.subscriptions(EEvent, e), self._regetit(e))
