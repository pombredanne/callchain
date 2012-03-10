# -*- coding: utf-8 -*-
'''linked chain assembly'''

from callchain.mixin.queued import QRootedMixin
from callchain.mixin.call import CallMixin, ECallMixin
from callchain.mixin.rooted import (
    RootedMixin, RootedChainMixin, ERootedChainMixin)
from callchain.mixin.fluent import FluentMixin, ChainMixin, EventMixin


class Linked(RootedMixin, FluentMixin, CallMixin):

    '''linked chain'''


class LinkedChain(RootedChainMixin, ChainMixin, CallMixin):

    '''linked call chain'''


class LinkedQ(LinkedChain, QRootedMixin):

    '''queued linked call chain'''


class Eventlink(ERootedChainMixin, EventMixin, ECallMixin):

    '''event link chain'''


class EventlinkQ(Eventlink, QRootedMixin):

    '''queued event link chain'''
