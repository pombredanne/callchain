# -*- coding: utf-8 -*-
'''manually balanced ordering linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.events import LinkMixin
from callchain.services.order import KRandom, KOrder

__all__ = ('randomevent', 'orderevent')


@appifies(KRandom)
class randomevent(LinkMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing linked event'''


@appifies(KOrder)
class orderevent(LinkMixin, ManQMixin, OrderMixin):

    '''manually balanced ordering linked event'''
