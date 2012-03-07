# -*- coding: utf-8 -*-
'''callchain event chain mixins'''

from callchain.octopus.core import InsideMixin
from callchain.octopus.resets import ResetLocalMixin
from callchain.chains.chain import LazyChainQMixin, ActiveChainQMixin

from callchain.events.core import EActiveMixin, ELazyMixin, EventRegistry


__all__ = ('ActiveEChainQMixin', 'LazyEChainQMixin', 'inside')


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
        # update event registry
        if events is not None:
            self.E.update(events)

    def _eventq(self, event):
        '''
        fetch call chain tied to `event`

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
        fetch callables bound to event

        @param event: event label
        '''
        return self.E.events(self.E.event(event))

    def event(self, event):
        '''
        create or fetch event

        @param event: event label
        '''
        self.E.event(event)
        return self

    def unevent(self, event):
        '''
        drop event

        @param event: event label
        '''
        self.E.unevent(event)
        return self


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
        that.E = EventRegistry('events')
        that.E.update(self.events)
        return that


class LazyEChainQMixin(ELazyMixin, EChainMixin, LazyChainQMixin):

    '''lazy event chain mixin'''


class ActiveEChainQMixin(EActiveMixin, EChainMixin, ActiveChainQMixin):

    '''active event chain mixin'''
