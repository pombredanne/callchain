# -*- coding: utf-8 -*-
'''synchronized ordering linked chains'''

from twoq.active.mixins import SyncQMixin
from twoq.mixins.ordering import RandomMixin, OrderMixin

from callchain.active.chains import ChainLinkMixin

__all__ = ('randomchain', 'orderchain')


class randomchain(ChainLinkMixin, SyncQMixin, RandomMixin):

    '''synchronized randomizing linked chain'''


class orderchain(ChainLinkMixin, SyncQMixin, OrderMixin):

    '''synchronized ordering linked chain'''
