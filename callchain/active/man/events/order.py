# -*- coding: utf-8 -*-
'''manually balanced ordering linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.events import AEventLinkMixin
from callchain.services.order import KRandom, KOrder

__all__ = ('randomevent', 'orderevent')


@appifies(KRandom)
class randomevent(AEventLinkMixin, AutoQMixin, RandomMixin):

    '''manually balanced randomizing linked event'''


@appifies(KOrder)
class orderevent(AEventLinkMixin, AutoQMixin, OrderMixin):

    '''manually balanced ordering linked event'''
