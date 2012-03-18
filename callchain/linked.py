# -*- coding: utf-8 -*-
'''linked chain assembly'''

from appspace.keys import appifies

from callchain.queued import QRootedMixin
from callchain.compact import CompactRootedMixin
from callchain.keys.linked import (
    KLinkedChain, KLinkedQ, KEventLink, KEventlinkQ)
from callchain.fluent import ChainMixin, EventMixin
from callchain.call import ChainCallMixin, EventCallMixin
from callchain.rooted import RootedMixin, EventRootedMixin


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


@appifies(KLinkedChain)
class chainlink(CompactRootedMixin, LinkedChain):

    '''root linked call chain'''


@appifies(KEventLink)
class eventlink(CompactRootedMixin, EventLink):

    '''root linked event chain'''
