# -*- coding: utf-8 -*-
'''call chain mixins'''

from threading import local

from callchain.core.octopus import tentacle, octopus

from callchain.mixins.keys import AChainLink

__all__ = ('CallChainMixin', 'ChainLinkMixin')


class ChainsQMixin(local):

    '''base call chain mixin'''

    def app(self, label, key=False):
        '''
        make application from appspace current call in chall chain

        @param label: application label
        @param key: key label (default: False)
        '''
        self._call = self.M.get(label, key)
        return self


class ChainLinkMixin(ChainsQMixin, tentacle):

    '''base linked call chain mixin'''


class CallChainMixin(ChainsQMixin, octopus):

    '''base call chain mixin'''

    def __init__(
        self, pattern, required=None, defaults=None, key=AChainLink, **kw
    ):
        '''
        init

        @param pattern: pattern configuration or appspace label
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(CallChainMixin, self).__init__(
            pattern, required, defaults, key, **kw
        )

    def link(self, label, branch):
        '''
        add linked call chain class

        @param label: linked call chain class label
        @param branch: linked call chain class
        '''
        self.M.ez_register(self._key, label, branch)
        return self

    def switch(self, label):
        '''
        switch to linked call chain

        @param label: chain label
        '''
        return self.M.lookup1(self._key, self._key, label)(self)
