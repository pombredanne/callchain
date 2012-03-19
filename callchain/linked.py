# -*- coding: utf-8 -*-
'''linked chains'''

from appspace.keys import appifies

from callchain.root import SingleMixin
from callchain.keys.linked import (
    KLinkedChain, KLinkedQ, KEventLink, KEventlinkQ)
from callchain.fluent import ChainMixin, EventMixin
from callchain.call import ChainCallMixin, EventCallMixin
from callchain.rooted import RootedMixin, EventRootedMixin, SingledMixin
from callchain.queued import QRootedMixin, ActiveContextMixin, LazyContextMixin


@appifies(KLinkedChain)
class LinkedChain(RootedMixin, ChainMixin, ChainCallMixin):

    '''linked call chain'''


@appifies(KLinkedQ)
class LinkedQ(QRootedMixin, LinkedChain):

    '''queued linked call chain'''


class LazyLinkedQ(LinkedQ, LazyContextMixin):

    '''lazy linked chain'''


class ActiveLinkedQ(LinkedQ, ActiveContextMixin):

    '''active linked chain'''


@appifies(KLinkedChain)
class chainlink(SingleMixin, SingledMixin, LinkedChain):

    '''root linked call chain'''


@appifies(KEventLink)
class EventLink(EventRootedMixin, EventMixin, EventCallMixin):

    '''event link chain'''


@appifies(KEventlinkQ)
class EventLinkQ(QRootedMixin, EventLink):

    '''queued event link chain'''


class ActiveEventLinkQ(EventLinkQ, ActiveContextMixin):

    '''active linked event'''


class LazyLinkedEventQ(EventLinkQ, LazyContextMixin):

    '''lazy linked event chain'''


@appifies(KEventLink)
class eventlink(SingledMixin, EventLink):

    '''root linked event chain'''
