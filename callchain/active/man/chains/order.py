# -*- coding: utf-8 -*-
'''manually balanced ordering linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.mixins.chains import AChainLinkMixin

__all__ = ('randomchain', 'orderchain')


class randomchain(AChainLinkMixin, AutoQMixin, RandomMixin):

    '''manually balanced randomizing linked chain'''


class orderchain(AChainLinkMixin, AutoQMixin, OrderMixin):

    '''manually balanced ordering linked chain'''
