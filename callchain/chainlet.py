# -*- coding: utf-8 -*-
'''chainlet and eventlet assembly'''

from appspace.keys import appifies, NoAppError

from callchain.resets import ResetLocalMixin
from callchain.fluent import EventMixin, ChainMixin
from callchain.keys.chain import KEventChain, KCallChain
from callchain.keys.chainlet import (
    KCallChainlet, KCallChainletQ, KEventlet, KEventletQ)
from callchain.rooted import SingledMixin, EventRootedMixin, RootedMixin
from callchain.queued import QRootedMixin, ActiveContextMixin, LazyContextMixin


class RootletMixin(ResetLocalMixin):

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


@appifies(KCallChainlet)
class Chainlet(RootletMixin, RootedMixin, ChainMixin):

    '''call chainlet'''


@appifies(KCallChainletQ)
class ChainletQ(QRootedMixin, Chainlet):

    '''queued call chainlet'''


class ActiveChainlet(ChainletQ, ActiveContextMixin):

    '''active chainlet'''


@appifies(KCallChain)
class chainlet(SingledMixin, Chainlet):

    '''root call chainlet'''


@appifies(KEventlet)
class Eventlet(RootletMixin, EventRootedMixin, EventMixin):

    '''eventlet'''


@appifies(KEventletQ)
class EventletQ(QRootedMixin, Eventlet):

    '''queued eventlet'''


class LazyChainlet(ChainletQ, LazyContextMixin):

    '''lazy chainlet'''


class ActiveEventlet(EventletQ, ActiveContextMixin):

    '''active eventlet'''


class LazyEventlet(EventletQ, LazyContextMixin):

    '''lazy eventlet'''


@appifies(KEventChain)
class eventlet(SingledMixin, Eventlet):

    '''root eventlet'''
