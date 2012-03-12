# -*- coding: utf-8 -*-
'''chainlet assembly'''

from callchain.mixin.queued import QRootedMixin
from callchain.mixin.rooted import (
    RootletMixin, ChainRootedMixin, EventRootedMixin)
from callchain.mixin.fluent import EventMixin, ChainMixin


class CallChainlet(ChainRootedMixin, RootletMixin, ChainMixin):

    '''call chainlet'''


class CallChainletQ(CallChainlet, QRootedMixin):

    '''queued call chainlet'''


class Eventlet(EventRootedMixin, RootletMixin, EventMixin):

    '''event chainlet'''


class EventletQ(Eventlet, QRootedMixin):

    '''queued event chainlet'''
