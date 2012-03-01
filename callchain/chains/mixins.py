# -*- coding: utf-8 -*-
'''call chain mixins'''

from appspace.keys import NoAppError

from octopus import Tentacle, Octopus
from octopus.resets import ResetLocalMixin

from callchain.chains.keys import KChainLink


__all__ = ('CallChainMixin', 'ChainLinkMixin')


class _Chain(ResetLocalMixin):

    '''base chain mixin'''

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            try:
                item = self._M.lookup1(self._key, self._key, label)
                if item is None:
                    raise NoAppError(label)
            except NoAppError:
                return self._getapp(label)
            else:
                return item(self)

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


class ChainLinkMixin(_Chain, Tentacle):

    '''base linked call chain mixin'''


class CallChainMixin(_Chain, Octopus):

    '''base call chain mixin'''

    def __init__(
        self, pattern, required=None, defaults=None, key=KChainLink, **kw
    ):
        '''
        init

        @param pattern: pattern configuration or appspace label
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        @param key: default key (default: KChainLink)
        '''
        super(CallChainMixin, self).__init__(
            pattern, required, defaults, key, **kw
        )

    def link(self, label, linked):
        '''
        add linked call chain class

        @param label: linked call chain class label
        @param branch: linked call chain class
        '''
        self.M.ez_register(self._key, label, linked)
        return self

    def switch(self, label):
        '''
        switch to linked call chain

        @param label: chain label
        '''
        return self.M.lookup1(self._key, self._key, label)(self)
