# -*- coding: utf-8 -*-
'''octopus'''

from twoq.support import port
from appspace.builders import Appspace
from stuf.utils import lazy, lazy_class, either

from callchain.core.paths import Pathways
from callchain.core.resets import ResetLocalMixin
from appspace.keys import AApp, AppLookupError, NoAppError

__all__ = ('octopus', 'tentacle', 'follow')


class follow(object):

    '''follow a specific call chain'''

    def __init__(self, pattern, required, defaults, key=AApp, *args, **kw):
        '''
        init

        @param pattern: pattern configuration class or appspace label
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        @param key: default appspace key (default: AApp)
        '''
        self.pattern = pattern
        self.required = required
        self.defaults = defaults
        self.key = key
        self.args = args
        self.kw = kw

    def __call__(self, that):
        # appspace manager
        that._M = Pathways.appspace(
            self.pattern,
            self.required,
            self.defaults,
            self.key,
            *self.args,
            **self.kw
        )
        that._K = self.key
        # lock octopus settings
        that._M.settings.lock()
        # octopus settings
        that._G = that._M.settings.final
        return that


class OctoMixin(ResetLocalMixin):

    def __getapp(self, label):
        try:
            item = self.M.get(label, self.M._current)
        except AppLookupError:
            try:
                # try finding namespace
                self.M.namespace(label)
            except AppLookupError:
                raise NoAppError(label)
            else:
                # temporarily swap primary label
                self.M._current = label
                return self
        else:
            # ensure current label is set back to default
            self.M._current = self.M._root
            return item

    @either
    def L(self):
        '''local manager settings'''
        return self.M.localize(self)

    @lazy
    def space(self):
        '''appspace'''
        return Appspace(self.M)

    def app(self, label, key=False):
        '''
        make application from appspace current call in chall chain

        @param label: application label
        @param key: key label (default: False)
        '''
        self._call = self.M.get(label, key)
        return self

    def add(self, app, label, key=False):
        '''
        add application to appspace

        @param app: new application
        @param label: application label
        @param key: key label (default: False)
        '''
        self.M.set(label, app, key)
        return self


class octopus(OctoMixin):

    '''appspace octopus'''

    def __init__(self, pattern, required=None, defaults=None, key=AApp, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(octopus, self).__init__()
        # application appspace
        self.M = Pathways.appspace(pattern, required, defaults, key)
        # freeze settings with any custom settings passed as keywords
        self.M.freeze(kw)

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            try:
                item = self.M.lookup1(self.key, self.key, label)
                if item is None:
                    raise NoAppError(label)
            except NoAppError:
                return self._getapp(label)
            else:
                return item(self)

    @property
    def G(self):
        '''application settings'''
        return self.M.settings.final

    @lazy_class
    def port(self):
        '''python 2.x <-> python 3.x compatibility helper'''
        return port


class tentacle(OctoMixin):

    '''appspace tentacle'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(tentacle, self).__init__()
        # octopus
        self.root = root
        # external manager appspace
        self.M = root.M
        # external manager local settings
        self.L = root.L
        # external manager global settings
        self.G = root.G
        # add internal root appspace
        self._M = root._M
        # add internal root settings
        self._G = root._G

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            return self._getapp(label)
