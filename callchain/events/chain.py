# -*- coding: utf-8 -*-
'''event chains'''

from callchain.octopus.core import InsideMixin
from callchain.chains.chain import LazyChainQMixin, ActiveChainQMixin

from callchain.events.core import ECoreMixin, ERunMixin

__all__ = ('ActiveEChainQMixin', 'LazyEChainQMixin', 'inside')


class EChainMixin(ECoreMixin, ERunMixin):

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

        @param patterns: pattern config or appspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(EChainMixin, self).__init__(
            patterns, required, defaults, *args, **kw
        )
        # local event registry
        self.E = events.build() if events is not None else None

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
            queue = self._chainlink(self)
            self.E.set(event, queue)
        return queue

    def _getevent(self, event):
        '''
        fetch callables bound to event

        @param event: event label
        '''
        return self.E.events(self._eget(event))

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
        that._E = self.events.build()
        return self._ocall(that)


class LazyEChainQMixin(EChainMixin, LazyChainQMixin):

    '''lazy event chain mixin'''


class ActiveEChainQMixin(EChainMixin, ActiveChainQMixin):

    '''active event chain mixin'''
