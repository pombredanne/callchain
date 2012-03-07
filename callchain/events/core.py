# -*- coding: utf-8 -*-
'''event core mixins'''

from itertools import chain

from stuf import orderedstuf
from stuf.utils import iterexcept
from appspace.keys import imap
from appspace import Patterns, Registry

from callchain.octopus import ResetLocalMixin

from callchain.chains.chain import callchain

from callchain.events.keys.events import EEvent

__all__ = ('ECoreMixin', 'EventRegistry')


class ECoreMixin(ResetLocalMixin):

    '''base event chain mixin'''

    _callchain = callchain

    def _events(self, *events):
        '''get callables bound to `*events`'''
        getit = self._getevent
        return chain(*tuple(imap(getit, events)))

    def commit(self):
        '''run event chain'''
        try:
            trigger = self.trigger
            fire = self.fire
            # 1. before event
            trigger('before')
            # 2. work event
            trigger('work')
            # everything else
            self._ocommit()
            # 3. change event
            fire('change')
            # 4. any event
            fire('any')
            # 5. after event
            fire('after')
        except:
            # 6. problem event
            fire('problem')
        finally:
            # 7. event that runs irrespective
            fire('anyway')
        return self

    def events(self, *events):
        '''
        ordered mapping of each event processing queue

        @param *events: event labels
        '''
        _eventq = self._eventq
        return orderedstuf((e, _eventq(e).queue) for e in events)

    def fire(self, *events):
        '''run callables bound to `*events` immediately'''
        try:
            # clear scratch queue
            self._sclear()
            # queue global and local bound callables
            self._sxtend(self._events(*events))
            # run event call chain until scratch queue is exhausted
            self._outextend(call() for call in iterexcept(
                self._scratch.popleft, IndexError
            ))
        finally:
            # clear scratch queue
            self._sclear()
        return self

    def on(self, event, call, key=False, *args, **kw):
        '''
        bind callable to event

        @param event: event label
        @param call: callable or eventspace label
        @param key: key label (default: False)
        '''
        self._eventq(event).chain(call, key, *args, **kw)
        return self

    def off(self, event):
        '''
        clear all callables bound to event

        @param event: event label
        '''
        self.E.unset(event)
        return self

    def trigger(self, *events):
        '''add callables bound to `*events` to main call chain'''
        self._cxtend(self._events(*events))
        return self


class EventRegistry(Registry):

    '''event registry'''

    __slots__ = ('_root', '_key')

    def __init__(self, label, key=EEvent):
        '''
        init

        @param label: label for event registry
        @param key: default key for event registry (default: EEvent)
        '''
        super(EventRegistry, self).__init__(label, key)

    def event(self, label):
        '''
        create or fetch event

        @param event: event label
        '''
        return self.key(self._key, label)

    def events(self, label):
        '''
        fetch things bound to event

        @param event: event label
        '''
        return self.subscriptions(self._key, label)

    def get(self, label):
        '''
        fetch thingto events

        @param event: event label
        '''
        key = self._key
        return self.lookup1(key, key, label)

    def set(self, label, call):
        '''
        bound thing to event

        @param event: event label
        @param call: some thing
        '''
        key = self._key
        self.register([key], key, label, call)

    def unevent(self, label):
        '''
        drop event

        @param event: event label
        '''
        self.E.unkey(self._key, label)

    def unset(self, label):
        '''
        clear all callables bound to event

        @param event: event label
        '''
        self.ez_unsubscribe(self._key, label)


class Pathways(Patterns):

    '''patterns for event registry'''

    _manager = EventRegistry
