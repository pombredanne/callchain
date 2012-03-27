# -*- coding: utf-8 -*-
'''root chain mixins'''

from operator import setitem

from stuf import frozenstuf
from stuf.utils import either, lazy

from callchain.patterns import Pathways

from callchain.mixins.resets import ResetLocalMixin


class ConfigMixin(ResetLocalMixin):

    '''configuration access mixin'''

    @lazy
    def defaults(self):
        '''default settings by their lonesome'''
        return self.M.settings.defaults if self.M is not None else frozenstuf()

    @lazy
    def required(self):
        '''required settings by their lonesome'''
        return self.M.settings.required if self.M is not None else frozenstuf()

    @either
    def G(self):
        '''external application global settings'''
        return self.M.settings.final if self.M is not None else frozenstuf()

    def _defaults(self):
        '''reset attribute values'''
        this = self.__dict__
        self.exhaustmap(
            vars(self),
            lambda x, y: setitem(this, x.rstrip('_d'), y),
            lambda x: x[0].endswith('_d'),
        )

    def _setdefault(self, key, value):
        '''
        set default value for instance attribute

        @param key: attribute name
        @param value: attribute value
        '''
        self.__dict__[key] = self.__dict__[key + '_d'] = value


class RootMixin(ConfigMixin):

    '''root chain mixin'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(RootMixin, self).__init__(pattern)
        if pattern is not None:
            # external appspace
            self.M = Pathways.appspace(pattern, required, defaults)
            # freeze external appspace global settings
            self.M.freeze(kw)
        else:
            self.M = None

    def __call__(self, *args):
        '''new chain session'''
        # clear call chain and queues and extend incoming things
        return self.clear().extend(args)
    
    def back(self, branch):
        '''
        handle switch from branch chain

        @param branch: branch chain
        '''
        self.clear()
        # extend root call chain with branch call chain
        self._chain.append(branch._chain)
        # sync with branch callable
        self._call = branch._call
        # sync with branch postitional arguments
        self._args = branch._args
        # sync with branch keyword arguments
        self._kw = branch._kw
        # sync with branch incoming and outgoing things
        return self.extend(branch.incoming).outextend(branch.outgoing)


class EventRootMixin(RootMixin):

    '''root event mixin'''

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
        super(EventRootMixin, self).__init__(
            patterns, required, defaults, *args, **kw
        )
        # update event registry with any other events
        if events is not None:
            self.E.update(events)

    def _eventq(self, event):
        '''
        linked chain bound to `event`

        @param event: event label
        '''
        key = self.E.event(event)
        # fetch linked chain bound to event
        queue = self.E.get(key)
        if queue is None:
            # create linked chain if nonexistent
            queue = self._linkedchain
            self.E.on(key, queue)
        return queue

    def _event(self, event):
        '''
        calls bound to `event`

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
