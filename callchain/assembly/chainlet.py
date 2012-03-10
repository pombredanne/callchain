# -*- coding: utf-8 -*-
'''chainlet assembly'''

from callchain.mixin.queued import QRootedMixin
from callchain.mixin.rooted import (
    RootedMixin, RootletMixin, RootedChainMixin, ERootedChainMixin)
from callchain.mixin.fluent import FluentMixin, EventMixin, ChainMixin


class Chainlet(RootletMixin, RootedMixin, FluentMixin):

    '''chain chainlet'''


class CallChainlet(RootletMixin, RootedChainMixin, ChainMixin):

    '''call chainlet'''


class CallChainletQ(CallChainlet, QRootedMixin):

    '''queued call chainlet'''


class Eventlet(RootletMixin, EventMixin, ERootedChainMixin):

    '''event chainlet'''


class EventletQ(Eventlet, QRootedMixin):

    '''queued event chainlet'''
