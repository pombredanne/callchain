# -*- coding: utf-8 -*-
'''chainlet assembly'''

from appspace.keys import appifies

from callchain.mixin.queued import QRootedMixin
from callchain.mixin.fluent import EventMixin, ChainMixin
from callchain.keys.chainlet import (
    KCallChainlet, KCallChainletQ, KEventlet, KEventletQ)
from callchain.mixin.rooted import RootletMixin, EventRootedMixin


@appifies(KCallChainlet)
class CallChainlet(RootletMixin, RootletMixin, ChainMixin):

    '''call chainlet'''


@appifies(KCallChainletQ)
class CallChainletQ(CallChainlet, QRootedMixin):

    '''queued call chainlet'''


@appifies(KEventlet)
class Eventlet(EventRootedMixin, RootletMixin, EventMixin):

    '''event chainlet'''


@appifies(KEventletQ)
class EventletQ(Eventlet, QRootedMixin):

    '''queued event chainlet'''
