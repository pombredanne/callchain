# -*- coding: utf-8 -*-
'''manually balanced ordering linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.chains.services.order import KRandom, KOrder

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('randomchain', 'orderchain')


@appifies(KRandom)
class randomchain(EventLinkMixin, ManQMixin, RandomMixin):

    '''manually balanced randomizing linked chain'''


@appifies(KOrder)
class orderchain(EventLinkMixin, ManQMixin, OrderMixin):

    '''manually balanced ordering linked chain'''
