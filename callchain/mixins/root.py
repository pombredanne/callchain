# -*- coding: utf-8 -*-
'''root chain mixins'''

from operator import setitem
from collections import deque

from stuf.core import frozenstuf
from twoq.active.mixins import ResultQMixin
from stuf.utils import either, lazy, exhaustmap

from callchain.patterns import Pathways
from callchain.mixins.resets import ResetLocalMixin
from callchain.mixins.core import QMixin


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

    def back(self, branch):
        '''
        handle branch chain switch

        @param branch: branch object
        '''
        self.clear()
        # extend root call chain with branch call chain
        self._cappend(branch._chain)
        return self

    _rback = back

    def _setdefault(self, key, value, default):
        '''
        set default value for instance attribute

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


class RootMixin(ConfigMixin):

    '''root chain mixin'''

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
        self._setup()

    def __call__(self, *args):
        '''new chain session'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self.extend(args)
        return self

    _r_call = __call__


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
            queue = self._callchain
            self.E.on(key, queue)
        return queue

    _e_eventq = _eventq

    def _event(self, event):
        '''
        calls bound to `event`

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
            
            
class LiteMixin(ResultQMixin):

    '''lite root chain mixin'''

    def _setup(self):
        '''configure chain'''
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


class QRootMixin(QMixin):

    '''queued root mixin'''

    def back(self, branch):
        '''
        handle switch from branch chain

        @param branch: branch chain
        '''
        self._rback(branch)
        # sync with branch callable
        self._call = branch._call
        # sync with branch postitional arguments
        self._args = branch._args
        # sync with branch keyword arguments
        self._kw = branch._kw
        # sync with branch incoming things
        self.extend(branch.incoming)
        # sync with branch outgoing things
        self.outextend(branch.outgoing)
        return self

    _qback = back