# -*- coding: utf-8 -*-
'''auto-balancing ordering linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.events import EventLinkMixin
from callchain.services.order import KRandom, KOrder

__all__ = ('randomevent', 'orderevent')


@appifies(KRandom)
class randomevent(EventLinkMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked event'''


@appifies(KOrder)
class orderevent(EventLinkMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked event'''
