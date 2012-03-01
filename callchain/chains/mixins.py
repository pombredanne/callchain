# -*- coding: utf-8 -*-
'''call chain mixins'''

from appspace.keys import NoAppError

from octopus import Tentacle, Octopus
from octopus.resets import ResetLocalMixin

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
        return self.M.lookup1(key, key, label)(self)
