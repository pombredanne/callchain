# -*- coding: utf-8 -*-
'''manually balanced ordering linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.chains import ChainLinkMixin
from callchain.services.order import KRandom, KOrder

__all__ = ('randomchain', 'orderchain')


@appifies(KRandom)
class randomchain(ChainLinkMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing linked chain'''


@appifies(KOrder)
class orderchain(ChainLinkMixin, ManQMixin, OrderMixin):

    '''manually balanced ordering linked chain'''
