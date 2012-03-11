# -*- coding: utf-8 -*-
'''chainlet assembly'''

from callchain.mixin.queued import QRootedMixin
from callchain.mixin.rooted import (
    RootletMixin, CRootedMixin, ERootedMixin)
from callchain.mixin.fluent import EventMixin, ChainMixin


class CallChainlet(CRootedMixin, RootletMixin, ChainMixin):

    '''call chainlet'''


class CallChainletQ(CallChainlet, QRootedMixin):

    '''queued call chainlet'''


class Eventlet(ERootedMixin, RootletMixin, EventMixin):

    '''event chainlet'''


class EventletQ(Eventlet, QRootedMixin):

    '''queued event chainlet'''
