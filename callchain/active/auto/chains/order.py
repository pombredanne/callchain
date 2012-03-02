# -*- coding: utf-8 -*-
'''auto-balancing ordering linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.chains import AChainLinkMixin
from callchain.services.order import KRandom, KOrder

__all__ = ('randomchain', 'orderchain')


@appifies(KRandom)
class randomchain(AChainLinkMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked chain'''


@appifies(KOrder)
class orderchain(AChainLinkMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked chain'''
