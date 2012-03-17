# -*- coding: utf-8 -*-
'''linked chain assembly'''

from appspace.keys import appifies

from callchain.mixin.queued import QRootedMixin
from callchain.keys.linked import (
    KLinkedChain, KLinkedQ, KEventLink, KEventlinkQ)
from callchain.mixin.fluent import ChainMixin, EventMixin
from callchain.mixin.call import ChainCallMixin, EventCallMixin
from callchain.mixin.rooted import RootedMixin, EventRootedMixin


@appifies(KLinkedChain)
class LinkedChain(RootedMixin, ChainMixin, ChainCallMixin):

    '''linked call chain'''


@appifies(KLinkedQ)
class LinkedQ(QRootedMixin, LinkedChain):

    '''queued linked call chain'''


@appifies(KEventLink)
class EventLink(EventRootedMixin, EventMixin, EventCallMixin):

    '''event link chain'''


@appifies(KEventlinkQ)
class EventLinkQ(QRootedMixin, EventLink):

    '''queued event link chain'''
