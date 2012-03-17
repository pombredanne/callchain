# -*- coding: utf-8 -*-
'''chainlet and eventlet assembly'''

from appspace.keys import appifies

from callchain.mixin.queued import QRootedMixin
from callchain.keys.chainlet import (
    KCallChainlet, KCallChainletQ, KEventlet, KEventletQ)
from callchain.mixin.fluent import EventMixin, ChainMixin
from callchain.mixin.rooted import RootletMixin, EventRootedMixin, RootedMixin


@appifies(KCallChainlet)
class CallChainlet(RootletMixin, RootedMixin, ChainMixin):

    '''call chainlet'''


@appifies(KCallChainletQ)
class CallChainletQ(QRootedMixin, CallChainlet):

    '''queued call chainlet'''


@appifies(KEventlet)
class Eventlet(RootletMixin, EventRootedMixin, EventMixin):

    '''eventlet'''


@appifies(KEventletQ)
class EventletQ(QRootedMixin, Eventlet):

    '''queued eventlet'''
