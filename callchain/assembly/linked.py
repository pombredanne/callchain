# -*- coding: utf-8 -*-
'''linked chain assembly'''

from callchain.mixin.queued import QRootedMixin
from callchain.mixin.call import CCallMixin, ECallMixin
from callchain.mixin.fluent import ChainMixin, EventMixin
from callchain.mixin.rooted import CRootedMixin, ERootedMixin


class LinkedChain(CRootedMixin, ChainMixin, CCallMixin):

    '''linked call chain'''


class LinkedQ(LinkedChain, QRootedMixin):

    '''queued linked call chain'''


class Eventlink(ERootedMixin, EventMixin, ECallMixin):

    '''event link chain'''


class EventlinkQ(Eventlink, QRootedMixin):

    '''queued event link chain'''
