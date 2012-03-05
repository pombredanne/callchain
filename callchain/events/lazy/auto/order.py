# -*- coding: utf-8 -*-
'''auto-balancing ordering linked event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.chains.services.order import KRandom, KOrder

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('randomevent', 'orderevent')


@appifies(KRandom)
class randomevent(EventLinkMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked event chain'''


@appifies(KOrder)
class orderevent(EventLinkMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked event chain'''
