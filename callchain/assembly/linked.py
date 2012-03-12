# -*- coding: utf-8 -*-
'''linked chain assembly'''

from appspace.keys import appifies

from callchain.mixin.queued import QRootedMixin
from callchain.keys.linked import (
    KLinkedChain, KLinkedQ, KEventlink, KEventlinkQ)
from callchain.mixin.fluent import ChainMixin, EventMixin
from callchain.mixin.call import ChainCallMixin, EventCallMixin
from callchain.mixin.rooted import ChainRootedMixin, EventRootedMixin


@appifies(KLinkedChain)
class LinkedChain(ChainRootedMixin, ChainMixin, ChainCallMixin):

    '''linked call chain'''


@appifies(KLinkedQ)
class LinkedQ(LinkedChain, QRootedMixin):

    '''queued linked call chain'''


@appifies(KEventlink)
class Eventlink(EventRootedMixin, EventMixin, EventCallMixin):

    '''event link chain'''


@appifies(KEventlinkQ)
class EventlinkQ(Eventlink, QRootedMixin):

    '''queued event link chain'''
