# -*- coding: utf-8 -*-
'''synchronized filtering linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.mixins.chains import AChainLinkMixin

__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


class collectchain(AChainLinkMixin, AutoQMixin, CollectMixin):

    '''synchronized collecting linked chain'''


class setchain(AChainLinkMixin, AutoQMixin, SetMixin):

    '''synchronized seting linked chain'''


class slicechain(AChainLinkMixin, AutoQMixin, SliceMixin):

    '''synchronized slicing linked chain'''


class filterchain(AChainLinkMixin, AutoQMixin, FilterMixin):

    '''synchronized filtering linked chain'''
