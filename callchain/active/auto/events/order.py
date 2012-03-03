# -*- coding: utf-8 -*-
'''auto-balancing ordering linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.events import LinkMixin
from callchain.services.order import KRandom, KOrder

__all__ = ('randomevent', 'orderevent')


@appifies(KRandom)
class randomevent(LinkMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked event'''


@appifies(KOrder)
class orderevent(LinkMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked event'''
