# -*- coding: utf-8 -*-
'''synchronized ordering linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.chains import ChainLinkMixin

__all__ = ('randomchain', 'orderchain')


class randomchain(ChainLinkMixin, AutoQMixin, RandomMixin):

    '''synchronized randomizing linked chain'''


class orderchain(ChainLinkMixin, AutoQMixin, OrderMixin):

    '''synchronized ordering linked chain'''
