# -*- coding: utf-8 -*-
'''synchronized ordering linked event chains'''

from twoq.active.mixins import SyncQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.events import LinkMixin

__all__ = ('randomevent', 'orderevent')


class randomevent(LinkMixin, SyncQMixin, RandomMixin):

    '''synchronized randomizing linked event'''


class orderevent(LinkMixin, SyncQMixin, OrderMixin):

    '''synchronized ordering linked event'''
