# -*- coding: utf-8 -*-
'''callchain managers'''

from itertools import starmap

from twoq import twoq
from stuf import stuf
from stuf.six import items, u
from appspace import Registry
from appspace.keys import AApp, ifilter
from stuf.utils import bi, getcls, lazy, exhaust
from appspace.managers import Manager as _Manager

from callchain.settings import Settings
from callchain.keys.event import EEvent
from callchain.keys.octopus import KSettings, KService, NoServiceError

__all__ = ['Manager']


class Manager(_Manager):

    '''callchain manager'''

    __slots__ = ('_current', '_root', '_key')

    def __init__(self, label, key=AApp):
        '''
        init

        @param label: label for appspace
        @param key: default key for appspace (default: AApp)
        '''
        super(Manager, self).__init__(label, key)
        self.ez_register(KSettings, label, Settings)

    @lazy
    def settings(self):
        '''get appspace settings'''
        return self.ez_lookup(KSettings, self._root)()

    @bi
    def localize(self, thing, *args, **kw):
        '''
        gather local settings from thing and its base classes, adding any
        passed settings

        @param thing: some thing with local settings
        '''
        return twoq([type.mro(getcls(thing)), [thing]]).smash().pick('Meta'
        ).members().tap(lambda x: not x[0].startswith('__')).filter().reup(
        ).wrap(stuf).map().invoke('update', *args, **kw).value()

    def freeze(self, *args, **kw):
        '''finalize settings, adding any passed settings'''

        self.settings.update(*args, **kw)
        self.settings.lock()

    def service(self, label):
        '''
        fetch service

        @param label: service label
        '''
        service = self.lookup1(KService, KService, label)
        if service is None:
            raise NoServiceError(label)
        return service


class Events(Registry):

    '''event registry'''

    __slots__ = ('_root', '_key')

    def __init__(self, label, key=EEvent):
        '''
        init

        @param label: label for event registry
        @param key: default key for event registry (default: EEvent)
        '''
        super(Events, self).__init__(label, key)

    def event(self, label):
        '''
        create or fetch event

        @param event: event label
        '''
        return self._unlazy(label, self._key, self.key(self._key, label))

    def events(self, key):
        '''
        fetch things bound to event

        @param label: event label
        '''
        return self.subscriptions(self._key, key)

    def get(self, key):
        '''
        fetch thing from events

        @param key: event key
        '''
        return self.lookup1(self._key, key)

    def set(self, key, call):
        '''
        bind thing to event

        @param label: event label 
        @param key: event key
        @param call: some thing
        '''
        self.register([self._key], key, call)
        
    def on(self, key, thing):
        '''
        bind thing to event

        @param label: event label 
        @param key: event key
        @param call: some thing
        '''
        self.subscribe(self._key, key, thing.commit)
        self.register([self._key], key, u(''), thing)

    def unevent(self, label):
        '''
        drop event

        @param event: event label
        '''
        self.E.unkey(self._key, self.event(label))

    def unset(self, label):
        '''
        clear all callables bound to event

        @param event: event label
        '''
        self.ez_unsubscribe(self._key, self.event(label))
        
    def pack(self, label, call):
        self.ez_register(self._key, label, self._lazy(call))

    def update(self, labels):
        '''
        update event registry with other events

        @param labels: eventconf
        '''
        pack = self.pack
        t = lambda x: not x[0].startswith('_')
        exhaust(starmap(pack, ifilter(t, items(vars(labels)))))
