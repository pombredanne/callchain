# -*- coding: utf-8 -*-
'''callchain chainlets and eventlets'''

from appspace.keys import NoAppError, appifies

# keys
from callchain.keys.chainlet import (
    KChainlet, KChainletQ, KEventlet, KEventletQ)
from callchain.keys.chain import KEventChain, KChain
# mixins
from callchain.resets import ResetLocalMixin
from callchain.fluent import EventMixin, ChainMixin
from callchain.queued import QBranchMixin, ActiveMixin, LazyMixin
from callchain.rooted import RootedMixin, EventBranchMixin, BranchMixin


class ChainletMixin(ResetLocalMixin):

    '''rootlet mixin'''

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

    def _synchback(self, key, value):
        '''
        sync with back

        @param key: key of value
        @param value: value of value
        '''
        self.__dict__[key] = self.root.__dict__[key] = value

    def back(self):
        '''revert to root chain'''
        return self.root.back(self)

    _rback = __rback = back


###############################################################################
## chainlets ##################################################################
###############################################################################

@appifies(KChainlet)
class Chainlet(ChainletMixin, BranchMixin, ChainMixin):

    '''chainlet'''


@appifies(KChain)
class chainlet(RootedMixin, Chainlet):

    '''root chainlet'''


@appifies(KChainletQ)
class ChainletQ(QBranchMixin, Chainlet):

    '''queued chainlet'''


class ActiveChainletQ(ChainletQ, ActiveMixin):

    '''active queued chainlet'''


class LazyChainletQ(ChainletQ, LazyMixin):

    '''lazy queued chainlet'''


###############################################################################
## eventlets ##################################################################
###############################################################################


@appifies(KEventlet)
class Eventlet(ChainletMixin, EventBranchMixin, EventMixin):

    '''eventlet'''


@appifies(KEventChain)
class eventlet(RootedMixin, Eventlet):

    '''root eventlet'''


@appifies(KEventletQ)
class EventletQ(QBranchMixin, Eventlet):

    '''queued eventlet'''


class ActiveEventletQ(EventletQ, ActiveMixin):

    '''active queued eventlet'''


class LazyEventletQ(EventletQ, LazyMixin):

    '''lazy queued eventlet'''
