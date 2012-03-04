# -*- coding: utf-8 -*-
'''octopus managers'''

from appspace import Patterns, Registry

from callchain.events.services import EEvent

__all__ = ['Register']


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

    _manager = Registry
