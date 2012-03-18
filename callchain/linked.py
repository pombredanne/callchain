# -*- coding: utf-8 -*-
'''linked chain assembly'''

from appspace.keys import appifies

from callchain.root import CompactRootMixin
from callchain.keys.linked import (
    KLinkedChain, KLinkedQ, KEventLink, KEventlinkQ)
from callchain.fluent import ChainMixin, EventMixin
from callchain.call import ChainCallMixin, EventCallMixin
from callchain.queued import QRootedMixin, ActiveContextMixin, LazyContextMixin
from callchain.rooted import RootedMixin, EventRootedMixin, CompactRootedMixin


@appifies(KLinkedChain)
class LinkedChain(RootedMixin, ChainMixin, ChainCallMixin):

    '''linked call chain'''


@appifies(KLinkedQ)
class LinkedQ(QRootedMixin, LinkedChain):

    '''queued linked call chain'''
    
    
class LazyLinked(LinkedQ, LazyContextMixin):

    '''lazy linked chain'''


class ActiveLinkedQ(LinkedQ, ActiveContextMixin):

    '''active linked chain'''


@appifies(KLinkedChain)
class chainlink(CompactRootMixin, CompactRootedMixin, LinkedChain):

    '''root linked call chain'''





@appifies(KEventLink)
class EventLink(EventRootedMixin, EventMixin, EventCallMixin):

    '''event link chain'''


@appifies(KEventlinkQ)
class EventLinkQ(QRootedMixin, EventLink):

    '''queued event link chain'''


class ActiveEventLinkQ(EventLinkQ, ActiveContextMixin):

    '''active linked event'''


class LazyLinkedEvent(EventLinkQ, LazyContextMixin):

    '''lazy linked event chain'''


@appifies(KEventLink)
class eventlink(CompactRootedMixin, EventLink):

    '''root linked event chain'''
