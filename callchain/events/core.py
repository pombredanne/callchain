# -*- coding: utf-8 -*-
'''event core mixins'''

from functools import partial
from collections import deque
from itertools import chain, starmap

from stuf.six import items
from stuf import orderedstuf
from appspace import Registry
from appspace.keys import imap, ifilter
from stuf.utils import iterexcept, exhaust

from callchain.octopus import ResetLocalMixin

from callchain.events.keys.events import EEvent

__all__ = ('ECoreMixin', 'EventRegistry')


class ECoreMixin(ResetLocalMixin):

    '''base event chain mixin'''

    @property
    def _callchain(self):
        return self._M.get('callchain', 'event')(self)

    def _events(self, *events):
        '''get callables bound to `*events`'''
        getit = self._event
        return chain(*tuple(imap(getit, events)))

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


class _ERunMixin(ECoreMixin):

    def commit(self):
        '''run event chain'''
        commit = self._ocommit
        try:
            trigger = self.trigger
            fire = self.fire
            # 1. before event
            trigger('before')
            # 2. work event
            trigger('work')
            # everything else
            commit()
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


class EActiveMixin(_ERunMixin):

    def fire(self, *events):
        '''run callables bound to `*events` immediately'''
        try:
            # clear scratch queue
            self._sclear()
            # queue global and local bound callables
            self._sxtend(self._events(*events))
            # run event call chain until scratch queue is exhausted
            self._outextend(call() for call in iterexcept(
                self._scratch.popleft, IndexError,
            ))
        finally:
            # clear scratch queue
            self._sclear()
        return self


class ELazyMixin(_ERunMixin):

    def fire(self, *events):
        '''run callables bound to `*events` immediately'''
        try:
            # clear scratch queue
            self._scratch = None
            # queue global and local bound callables
            self._scratch = deque(self._events(*events))
            # run event call chain until scratch queue is exhausted
            self.outgoing = deque(call() for call in iterexcept(
                self._scratch.popleft, IndexError,
            ))
        finally:
            # clear scratch queue
            self._scratch = None
        return self


class ERootedMixin(ResetLocalMixin):

    '''linked event chain'''

    def __init__(self, root):
        '''
        init

        @param root: root event chain
        '''
        super(ERootedMixin, self).__init__(root)
        # root event chain getter
        self._regetit = self.root._event
        # event getter
        self._eget = self.root.event
        # local event registry
        self.E = EventRegistry('events')

    def _eventq(self, event):
        '''
        fetch chain tied to `event`

        @param event: event label
        '''
        # fetch event from root call chain
        event = self._eget(event)
        # fetch linked call chain bound to event
        queue = self.E.get(event)
        if queue is None:
            # create liked call chain if nonexistent
            queue = self._callchain(self)
            self.E.set(event, queue)
        return queue

    def _event(self, event):
        '''
        fetch callables bound to event

        @param event: event label
        '''
        e = self._eget(event)
        return chain(self.E.events(e), self._regetit(e))


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

    def update(self, events):
        ez_register = partial(self.ez_register, self._key)
        t = lambda x: not x[0].startswith('_')
        exhaust(starmap(ez_register, ifilter(t, items(vars(events)))))
