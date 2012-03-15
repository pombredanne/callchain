# -*- coding: utf-8 -*-
'''manager mixins'''

from operator import setitem

from stuf.core import frozenstuf
from stuf.utils import either, lazy, exhaustmap

from callchain.patterns import Pathways

from callchain.mixin.reset import ResetLocalMixin


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

    def _setdefault(self, key, value, default):
        value = value if value is not None else default
        self.__dict__[key] = value
        self.__dict__[key + '_d'] = value

    _osetdefault = _setdefault

    def _resetdefaults(self):
        this = self.__dict__
        exhaustmap(
            vars(self),
            lambda x, y: setitem(this, x.rstrip('_d'), y),
            lambda x: x[0].endswith('_d'),
        )
        
    _oresetdefaults = _resetdefaults


class ChainManageMixin(ManagerMixin):

    '''chain manager mixin'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(ChainManageMixin, self).__init__(
            pattern, required, defaults, **kw
        )
        self._setup_chain()


class EventManageMixin(ChainManageMixin):

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
