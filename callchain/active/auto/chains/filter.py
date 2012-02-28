# -*- coding: utf-8 -*-
'''auto-balancing filtering linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.mixins.chains import AChainLinkMixin

__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


class collectchain(AChainLinkMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked chain'''


class setchain(AChainLinkMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked chain'''


class slicechain(AChainLinkMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked chain'''


class filterchain(AChainLinkMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked chain'''
