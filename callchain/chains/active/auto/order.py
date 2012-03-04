# -*- coding: utf-8 -*-
'''auto-balancing ordering linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.services.order import KRandom, KOrder

from callchain.chains.active.mixins import ChainLinkMixin

__all__ = ('randomchain', 'orderchain')


@appifies(KRandom)
class randomchain(ChainLinkMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked chain'''


@appifies(KOrder)
class orderchain(ChainLinkMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked chain'''
