# -*- coding: utf-8 -*-
'''call chain mixins'''

from octopus import Tentacle, Octopus
from octopus.keys import NoServiceError
from octopus.resets import ResetLocalMixin

__all__ = ('CallChainMixin', 'ChainLinkMixin')


class _Chain(ResetLocalMixin):

    '''base chain mixin'''

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            try:
                # silent switch
                key = self._M.service(label)
                item = self._M.lookup1(key, key)(self)
                return getattr(item, label)
            except NoServiceError:
                return super(_Chain, self).__getattr__(label)

    def tap(self, call, key=False):
        '''
        make application from appspace current call in chall chain

        @param label: application label
        @param key: key label (default: False)
        '''
        self._call = self.M.get(call, key)
        return self


class ChainLinkMixin(_Chain, Tentacle):

    '''base linked call chain mixin'''


class CallChainMixin(_Chain, Octopus):

    '''base call chain mixin'''

    def switch(self, label, key=False):
        '''
        switch to linked call chain

        @param label: chain label
        '''
        key = self.M.namespace(key)
        return self.M.lookup1(key, key, label)(self)
