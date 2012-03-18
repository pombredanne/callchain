# -*- coding: utf-8 -*-
'''chainlet and eventlet assembly'''

from appspace.keys import appifies

from callchain.queued import QRootedMixin
from callchain.keys.chainlet import (
    KCallChainlet, KCallChainletQ, KEventlet, KEventletQ)
from callchain.fluent import EventMixin, ChainMixin
from callchain.compact import CompactRootedMixin
from callchain.keys.chain import KEventChain, KCallChain
from callchain.rooted import RootletMixin, EventRootedMixin, RootedMixin


@appifies(KCallChainlet)
class Chainlet(RootletMixin, RootedMixin, ChainMixin):

    '''call chainlet'''


@appifies(KCallChainletQ)
class ChainletQ(QRootedMixin, Chainlet):

    '''queued call chainlet'''


@appifies(KEventlet)
class Eventlet(RootletMixin, EventRootedMixin, EventMixin):

    '''eventlet'''


@appifies(KEventletQ)
class EventletQ(QRootedMixin, Eventlet):

    '''queued eventlet'''


@appifies(KCallChain)
class chainlet(CompactRootedMixin, Chainlet):

    '''root call chainlet'''


@appifies(KEventChain)
class eventlet(CompactRootedMixin, Eventlet):

    '''root eventlet'''
