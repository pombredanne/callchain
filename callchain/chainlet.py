# -*- coding: utf-8 -*-
'''callchain chainlets and eventlets'''

from appspace.keys import NoAppError, appifies

# keys
from callchain.keys.chainlet import (
    KChainlet, KChainletQ, KEventlet, KEventletQ)
from callchain.keys.chain import KEventChain, KChain
# mixins
from callchain.queued import QBranchMixin
from callchain.resets import ResetLocalMixin
from callchain.fluent import EventMixin, ChainMixin
from callchain.branch import LitedMixin, EventBranchMixin, BranchMixin


class ChainletMixin(ResetLocalMixin):

    '''chainlet mixin'''

    def _load(self, label):
        '''
        silent internal switch back...

        @param label: appspaced thing label
        '''
        # fetch appspaced thing...
        try:
            return self._f_load(label)
        # ...or revert to root chain
        except NoAppError:
            return getattr(self.__rback(), label)

    _r_load = _load

    def _syncback(self, key, value):
        '''
        sync chainlet with root chain

        @param key: key of value
        @param value: value of value
        '''
        self.__dict__[key] = self.root.__dict__[key] = value

    _r_syncback = _syncback

    def back(self):
        '''switch to root chain'''
        return self.root.back(self)

    _rback = __rback = back


###############################################################################
## chainlets ##################################################################
###############################################################################

@appifies(KChainlet)
class Chainlet(ChainletMixin, BranchMixin, ChainMixin):

    '''chainlet'''


@appifies(KChain)
class chainlet(LitedMixin, Chainlet):

    '''root chainlet'''


@appifies(KChainletQ)
class ChainletQ(QBranchMixin, Chainlet):

    '''queued chainlet'''


###############################################################################
## eventlets ##################################################################
###############################################################################


@appifies(KEventlet)
class Eventlet(ChainletMixin, EventBranchMixin, EventMixin):

    '''eventlet'''


@appifies(KEventChain)
class eventlet(LitedMixin, Eventlet):

    '''root eventlet'''


@appifies(KEventletQ)
class EventletQ(QBranchMixin, Eventlet):

    '''queued eventlet'''
