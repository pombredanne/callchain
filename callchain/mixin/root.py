# -*- coding: utf-8 -*-
'''chain mixins'''

from stuf.utils import either
from stuf.core import frozenstuf

from callchain.patterns import Pathways

from callchain.mixin.reset import ResetLocalMixin


class RootMixin(ResetLocalMixin):

    '''root chain'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(RootMixin, self).__init__()
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


class RootChainMixin(RootMixin):

    '''root call chain mixin'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(RootChainMixin, self).__init__(pattern, required, defaults, **kw)
        self._setup_chain()

    def __call__(self, *args):
        '''new chain session'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self.extend(args)
        return self

    _dcall = __call__

    def back(self, link):
        '''
        handle chainlet end

        @param link: linked call chain
        '''
        self.clear()
        # extend call chain with root call chain
        self._cappend(link._chain)
        self._qback(link)
        return self

    _rback = back


class RootEventMixin(RootChainMixin):

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
        super(RootEventMixin, self).__init__(
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
            # create liked call chain if nonexistent
            queue = self._callchain
            self.E.on(key, queue)
        return queue

    _eeventq = _eventq

    def _event(self, event):
        '''
        fetch calls bound to `event`

        @param event: event label
        '''
        return self.E.events(self.E.event(event))

    _devent = _event

    def event(self, event):
        '''
        create or fetch `event`

        @param event: event label
        '''
        self.E.event(event)
        return self

    _eevent = event

    def unevent(self, event):
        '''
        drop `event`

        @param event: event label
        '''
        self.E.unevent(event)
        return self

    _eunevent = unevent
