# -*- coding: utf-8 -*-
'''callchain octopus managers'''

from functools import partial
from itertools import starmap

from twoq import twoq
from stuf import stuf
from stuf.six import items
from appspace import Registry
from appspace.keys import AApp, ifilter
from stuf.utils import bi, getcls, lazy, exhaust
from appspace.managers import Manager as _Manager

from callchain.settings import Settings
from callchain.keys.events.events import EEvent
from callchain.keys.octopus import KSettings, KService, NoServiceError

__all__ = ['Manager']


class Manager(_Manager):

    '''octopus manager'''

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
        return self.key(self._key, label)

    def events(self, label):
        '''
        fetch things bound to event

        @param event: event label
        '''
        return self.subscriptions(self._key, label)

    def get(self, label):
        '''
        fetch thing from events

        @param event: event label
        '''
        key = self._key
        return self.lookup1(key, key, label)

    def set(self, label, call):
        '''
        bind thing to event

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

    def update(self, labels):
        '''
        update event registry with other events

        @param labels: eventconf
        '''
        ez_register = partial(self.ez_register, self._key)
        t = lambda x: not x[0].startswith('_')
        exhaust(starmap(ez_register, ifilter(t, items(vars(labels)))))