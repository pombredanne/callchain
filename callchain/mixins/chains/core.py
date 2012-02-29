# -*- coding: utf-8 -*-
'''call chain mixins'''

from callchain.core.octopus import tentacle, octopus

from callchain.mixins.chains.keys import AChainLink

__all__ = ('CallChainMixin', 'ChainLinkMixin')


class ChainLinkMixin(tentacle):

    '''base linked call chain mixin'''


class CallChainMixin(octopus):

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
