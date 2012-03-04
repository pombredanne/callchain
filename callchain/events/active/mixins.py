# -*- coding: utf-8 -*-
'''active event chains'''

from stuf.utils import iterexcept
from octopus.resets import ResetLocalMixin

from callchain.events.mixins import ELinkMixin, EChainMixin
from callchain.chains.active.mixins import ChainLinkMixin, CallChainMixin


class _EventMixin(ResetLocalMixin):

    '''base event chain mixin'''

    ###########################################################################
    ## event chain execution ##################################################
    ###########################################################################

    def fire(self, *events):
        '''run callables bound to `*events` immediately'''
        try:
            # clear scratch queue
            self._sclear()
            # queue global and local bound callables
            self._sxtend(self._events(*events))
            # run event call chain until scratch queue is exhausted
            calls = iterexcept(self._scratch.popleft, IndexError)
            self.outappend(call() for call in calls)
        finally:
            # clear scratch queue
            self._sclear()
        return self

    def trigger(self, *events):
        '''add callables bound to `*events` to main call chain'''
        self._cxtend(self._events(*events))
        return self


class EventLinkMixin(_EventMixin, ELinkMixin, ChainLinkMixin):

    '''linked event chain mixin'''


class EventChainMixin(_EventMixin, EChainMixin, CallChainMixin):

    '''event chain mixin'''
