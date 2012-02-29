# -*- coding: utf-8 -*-
'''auto-balancing ordering linked event chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.mixins.events import AEventLinkMixin

__all__ = ('randomevent', 'orderevent')


class randomevent(AEventLinkMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked event'''


class orderevent(AEventLinkMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked event'''