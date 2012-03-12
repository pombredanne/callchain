# -*- coding: utf-8 -*-
'''linked chain assembly'''

from callchain.mixin.queued import QRootedMixin
from callchain.mixin.fluent import ChainMixin, EventMixin
from callchain.mixin.call import ChainCallMixin, EventCallMixin
from callchain.mixin.rooted import ChainRootedMixin, EventRootedMixin


class LinkedChain(ChainRootedMixin, ChainMixin, ChainCallMixin):

    '''linked call chain'''


class LinkedQ(LinkedChain, QRootedMixin):

    '''queued linked call chain'''


class Eventlink(EventRootedMixin, EventMixin, EventCallMixin):

    '''event link chain'''


class EventlinkQ(Eventlink, QRootedMixin):

    '''queued event link chain'''
