# -*- coding: utf-8 -*-
'''manually balanced ordering linked event chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.events import AEventLinkMixin

__all__ = ('randomevent', 'orderevent')


class randomevent(AEventLinkMixin, AutoQMixin, RandomMixin):

    '''manually balanced randomizing linked event'''


class orderevent(AEventLinkMixin, AutoQMixin, OrderMixin):

    '''manually balanced ordering linked event'''
