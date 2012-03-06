# -*- coding: utf-8 -*-
'''event chains'''

from callchain.chains.chain import (
    callchain, LazyChainQMixin, ActiveChainQMixin)

from callchain.events.core import ECoreMixin

__all__ = ('ActiveEChainQMixin', 'LazyEChainQMixin', 'eventchain')


class _EChainMixin(ECoreMixin):

    '''event chain'''

    def __init__(
        self, patterns=None, events=None, required=None, defaults=None, *args,
        **kw
    ):
        '''
        init

        @param patterns: pattern config or appspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(_EChainMixin, self).__init__(
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


class eventchain(_EChainMixin, callchain):

    '''event chain'''


class LazyEChainQMixin(_EChainMixin, LazyChainQMixin):

    '''lazy event chain mixin'''


class ActiveEChainQMixin(_EChainMixin, ActiveChainQMixin):

    '''active event chain mixin'''
