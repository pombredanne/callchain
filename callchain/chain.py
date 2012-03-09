# -*- coding: utf-8 -*-
'''callchains root call chain mixins'''

from stuf.utils import either
from stuf.core import frozenstuf

from callchain.patterns import Pathways

from callchain.call import QCallingMixin, ECallingMixin, CallMixin


class Chain(CallMixin):

    '''root chain'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(Chain, self).__init__()
        if pattern is not None:
            # external appspace
            self.M = Pathways.appspace(pattern, required, defaults)
            # freeze external appspace global settings
            self.M.freeze(kw)
        else:
            self.M = None

    @either
    def G(self):
        '''external application global settings'''
        return self.M.settings.final if self.M is not None else frozenstuf()


class ChainMixin(Chain):

    '''root call chain mixin'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(ChainMixin, self).__init__(pattern, required, defaults, **kw)
        self._setup_chain()

    def back(self, link):
        '''
        handle return from linked call chain

        @param link: linked call chain
        '''
        self.clear()
        # extend call chain with root call chain
        self._cappend(link._chain)
        return self

    _oback = back


class ChainQMixin(ChainMixin, QCallingMixin):

    '''queued root call chain mixin'''

    def back(self, link):
        '''
        handle return from linked call chain

        @param link: linked call chain
        '''
        self._oback(link)
        # sync with link callable
        self._call = link._call
        # sync with link postitional arguments
        self._args = link._args
        # sync with link keyword arguments
        self._kw = link._kw
        return self

    _cback = back


class EChainMixin(ChainMixin, ECallingMixin):

    '''root event chain mixin'''

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
        # fetch linked call chain bound to event
        key = self.E.event(event)
        queue = self.E.get(key)
        if queue is None:
            # create linked call chain if nonexistent
            queue = self._callchain
            self.E.set(key, queue)
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
