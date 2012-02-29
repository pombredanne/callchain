# -*- coding: utf-8 -*-
'''auto-balancing ordering linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.chains import AChainLinkMixin

__all__ = ('randomchain', 'orderchain')


class randomchain(AChainLinkMixin, AutoQMixin, RandomMixin):

    '''auto-balancing randomizing linked chain'''


class orderchain(AChainLinkMixin, AutoQMixin, OrderMixin):

    '''auto-balancing ordering linked chain'''
