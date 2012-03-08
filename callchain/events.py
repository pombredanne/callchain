# -*- coding: utf-8 -*-
'''callchain event mixins'''

from itertools import chain

from stuf import orderedstuf
from appspace.keys import imap

from callchain.managers import Events
from callchain.octopus import InsideMixin
from callchain.resets import ResetLocalMixin


class inside(InsideMixin):

    '''internal eventspace configuration'''

    def __init__(
        self,
        patterns=None,
        events=None,
        required=None,
        defaults=None,
        *args,
        **kw
    ):
        '''
        init

        @param patterns: pattern config or appspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(inside, self).__init__(patterns, required, defaults, *args, **kw)
        self.events = events

    def __call__(self, that):
        that = self._ocall(that)
        that.E = Events('events')
        that.E.update(self.events)
        return that


class EventMixin(ResetLocalMixin):

    '''event chain mixin'''

    @property
    def _callchain(self):
        '''new linked event chain'''
        return self._M.get('callchain', 'event')(self)

    def _events(self, *events):
        '''get callables bound to `*events`'''
        return chain(*tuple(imap(self._event, events)))

    def on(self, event, call, key=False, *args, **kw):
        '''
        bind calls to `event`

        @param event: event label
        @param call: callable or eventspace label
        @param key: key label (default: False)
        '''
        self._eventq(event).chain(call, key, *args, **kw)
        return self

    def off(self, event):
        '''
        clear all calls bound to `event`

        @param event: event label
        '''
        self.E.unset(event)
        return self

    def trigger(self, *events):
        '''add calls bound to `*events` to primary call chain'''
        self._cxtend(self._events(*events))
        return self


class ERunMixin(EventMixin):

    '''event chain execution mixin'''

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
        return orderedstuf((e, self._eventq(e).queue) for e in events)


class ERootedMixin(ResetLocalMixin):

    '''rooted event chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root event chain
        '''
        super(ERootedMixin, self).__init__(root)
        # root event chain fetcher
        self._regetit = self.root._event
        # event getter
        self._eget = self.root.event
        # local event registry
        self.E = Events('events')

    def _eventq(self, event):
        '''
        fetch linked chain tied to `event`

        @param event: event label
        '''
        # fetch event from root event chain
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
        fetch calls bound to `event`

        @param event: event label
        '''
        e = self._eget(event)
        return chain(self.E.events(e), self._regetit(e))


class EChainMixin(ResetLocalMixin):

    '''event chain mixin'''

    def __init__(
        self,
        patterns=None,
        events=None,
        required=None,
        defaults=None,
        *args,
        **kw
    ):
        '''
        init

        @param patterns: pattern config or eventspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(EChainMixin, self).__init__(
            patterns, required, defaults, *args, **kw
        )
        # update event registry with any other events
        if events is not None:
            self.E.update(events)

    def _eventq(self, event):
        '''
        fetch linked call chain tied to `event`

        @param event: event label
        '''
        # fetch event
        event = self.event(event)
        # fetch linked call chain bound to event
        queue = self.E.get(event)
        if queue is None:
            # create linked call chain if nonexistent
            queue = self._callchain
            self.E.set(event, queue)
        return queue

    def _event(self, event):
        '''
        fetch calls bound to `event`

        @param event: event label
        '''
        return self.E.events(self.E.event(event))

    def event(self, event):
        '''
        create or fetch `event`

        @param event: event label
        '''
        self.E.event(event)
        return self

    def unevent(self, event):
        '''
        drop `event`

        @param event: event label
        '''
        self.E.unevent(event)
        return self
