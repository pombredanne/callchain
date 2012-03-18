# -*- coding: utf-8 -*-
'''root mixins'''

from operator import setitem
from collections import deque

from stuf.core import frozenstuf
from twoq.active.mixins import ResultQMixin
from stuf.utils import either, lazy, exhaustmap

from callchain.patterns import Pathways
from callchain.internal import ResetLocalMixin


class RootMixin(ResetLocalMixin):

    '''root chain mixin'''

    def __call__(self, *args):
        '''new chain session'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self.extend(args)
        return self

    _r_call = __call__

    def back(self, link):
        '''
        handle chainlet end

        @param link: linked chain
        '''
        self.clear()
        # extend call chain with root call chain
        self._cappend(link._chain)
        return self

    _rback = back


class EventRootMixin(RootMixin):

    '''root event mixin'''

    def _eventq(self, event):
        '''
        fetch linked call chain tied to `event`

        @param event: event label
        '''
        key = self.E.event(event)
        # fetch linked call chain bound to event
        queue = self.E.get(key)
        if queue is None:
            # create liked call chain if nonexistent
            queue = self._callchain
            self.E.on(key, queue)
        return queue

    _e_eventq = _eventq

    def _event(self, event):
        '''
        fetch calls bound to `event`

        @param event: event label
        '''
        return self.E.events(self.E.event(event))

    _e_event = _event

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


class ManagerMixin(ConfigMixin):

    '''manager mixin'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(ManagerMixin, self).__init__()
        if pattern is not None:
            # external appspace
            self.M = Pathways.appspace(pattern, required, defaults)
            # freeze external appspace global settings
            self.M.freeze(kw)
        else:
            self.M = None
        self._setup()

    def _setdefault(self, key, value, default):
        '''
        set default value for an instance attribute

        @param key: attribute name
        @param value: attribute value
        @param default: default value
        '''
        value = value if value is not None else default
        self.__dict__[key] = value
        self.__dict__[key + '_d'] = value

    _m_setdefault = _setdefault

    def _defaults(self):
        '''reset attribute values'''
        this = self.__dict__
        exhaustmap(
            vars(self),
            lambda x, y: setitem(this, x.rstrip('_d'), y),
            lambda x: x[0].endswith('_d'),
        )

    _m_defaults = _defaults


class EventManageMixin(ManagerMixin):

    '''event manager mixin'''

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
        super(EventManageMixin, self).__init__(
            patterns, required, defaults, *args, **kw
        )
        # update event registry with any other events
        if events is not None:
            self.E.update(events)
            
            
class CompactRootMixin(ResultQMixin):

    '''base root chain mixin'''

    def _setup(self):
        '''setup chain'''
        self.outgoing = deque()
        # outgoing things right extend
        self.outextend = self.outgoing.extend
        # outgoing things clear
        self._outclear = self.outgoing.clear
        # outgoing things right append
        self._outappend = self.outgoing.append
        # outgoing things left pop
        self.popleft = self.outgoing.popleft
        self._c_setup()

    _d_setup = _setup