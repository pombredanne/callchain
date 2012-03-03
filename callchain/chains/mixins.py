# -*- coding: utf-8 -*-
'''call chain mixins'''

from appspace.keys import NoAppError
from octopus import Tentacle, Octopus
from octopus.keys import NoServiceError

__all__ = ('EventChainMixin', 'LinkMixin')


class LinkMixin(Tentacle):

    '''base linked call chain mixin'''

    def _iget(self, label):
        try:
            # silent switch
            _M = self._M
            key = _M.service(label)
            return getattr(_M.get(key, key)(self), label)
        except NoServiceError:
            try:
                return super(LinkMixin, self)._iget(label)
            except NoAppError:
                return getattr(self.back(), label)

    def back(self):
        '''back to root call chain'''
        self = self.root.back(self)
        return self


class EventChainMixin(Octopus):

    '''base call chain mixin'''

    def _iget(self, label):
        try:
            # silent switch
            _M = self._M
            key = _M.service(label)
            return getattr(_M.get(key, key)(self), label)
        except NoServiceError:
            return super(EventChainMixin, self)._iget(label)

    def switch(self, label, key=False):
        '''
        switch to linked call chain

        @param label: chain label
        @param key: chain key (default: False)
        '''
        return self.M.get(label, key)(self)
