# -*- coding: utf-8 -*-
'''auto-balancing ordering linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.chains.services.order import KRandom, KOrder

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('randomchain', 'orderchain')


@appifies(KRandom)
class randomchain(EventLinkMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked chain'''


@appifies(KOrder)
class orderchain(EventLinkMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked chain'''
