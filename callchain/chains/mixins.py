# -*- coding: utf-8 -*-
'''call chain mixins'''

from stuf.six import strings
from appspace.keys import NoAppError
from octopus import Tentacle, Octopus
from octopus.keys import NoServiceError
from octopus.resets import ResetLocalMixin

__all__ = ('CChainMixin', 'CLinkMixin')


class _CChainMixin(ResetLocalMixin):

    '''chain mixin'''

    def tap(self, call, branch=False):
        '''
        add call

        @param call: callable or appspace label
        @param key: linked call chain chain key (default: False)
        '''
        # reset postitional arguments
        self._args = ()
        # reset keyword arguments
        self._kw = {}
        # set current application
        self._app = self._M.get(
            call, branch
        ) if isinstance(call, strings) else call
        return self

    _cctap = tap


class CLinkMixin(_CChainMixin, Tentacle):

    '''linked call chain mixin'''

    def _iget(self, label):
        '''
        silent internal switch back...

        @param label: appspaced thing label
        '''
        # lookup appspaced thing...
        try:
            return self._oiget(label)
        #...or return to root chain
        except NoAppError:
            return getattr(self.back(), label)

    _cciget = _iget

    def back(self):
        '''return to root call chain'''
        self = self.root.back(self)
        return self

    _oback = back


class CChainMixin(_CChainMixin, Octopus):

    '''call chain mixin'''

    def _iget(self, label):
        '''
        silent internal switch to...

        @param label: appspaced thing label
        '''
        try:
            # look up internally linked call chains...
            _M = self._M
            key = _M.service(label)
            return getattr(_M.get(key, key)(self), label)
        except NoServiceError:
            # ...or lookup other appspace things
            return self._oiget(label)

    _cciget = _iget

    def switch(self, label, key=False):
        '''
        overt switch to linked call chain from external appspace

        @param label: linked call chain label
        @param key: linked call chain chain key (default: False)
        '''
        return self.M.get(label, key)(self)

    _oswitch = switch
