# -*- coding: utf-8 -*-
'''call chain mixins'''

from octopus import Tentacle, Octopus
from octopus.keys import NoServiceError
from octopus.resets import ResetLocalMixin
from appspace.keys import NoAppError

__all__ = ('ChainMixin', 'LinkMixin')


class _Chain(ResetLocalMixin):

    '''base chain mixin'''


class LinkMixin(_Chain, Tentacle):

    '''base linked call chain mixin'''

    def _iget(self, label):
        try:
            # silent switch
            _M = self._M
            key = _M.service(label)
            item = _M.get(key, key)(self)
            item = getattr(item, label)
            return item
        except NoServiceError:
            try:
                return super(LinkMixin, self)._iget(label)
            except NoAppError:
                return self.back()


class ChainMixin(_Chain, Octopus):

    '''base call chain mixin'''

    def _iget(self, label):
        try:
            # silent switch
            _M = self._M
            key = _M.service(label)
            item = _M.get(key, key)(self)
            item = getattr(item, label)
            return item
        except NoServiceError:
            return super(ChainMixin, self)._iget(label)

    def switch(self, label, key=False):
        '''
        switch to linked call chain

        @param label: chain label
        @param key: chain key (default: False)
        '''
        M = self._M
        key = M.namespace(key)
        return M.lookup1(key, key, label)(self)
