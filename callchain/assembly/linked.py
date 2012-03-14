# -*- coding: utf-8 -*-
'''linked chain assembly'''

from appspace.keys import appifies

from callchain.mixin.root import BackRootMixin
from callchain.mixin.queued import QRootedMixin
from callchain.keys.linked import (
    KLinkedChain, KLinkedQ, KEventLink, KEventlinkQ)
from callchain.mixin.fluent import ChainMixin, EventMixin
from callchain.mixin.call import ChainCallMixin, EventCallMixin
from callchain.mixin.rooted import ChainRootedMixin, EventRootedMixin


@appifies(KLinkedChain)
class LinkedChain(ChainRootedMixin, ChainMixin, BackRootMixin, ChainCallMixin):

    '''linked call chain'''


@appifies(KLinkedQ)
class LinkedQ(LinkedChain, QRootedMixin):

    '''queued linked call chain'''


@appifies(KEventLink)
class EventLink(EventRootedMixin, EventMixin, BackRootMixin, EventCallMixin):

    '''event link chain'''


@appifies(KEventlinkQ)
class EventLinkQ(EventLink, QRootedMixin):

    '''queued event link chain'''
