# -*- coding: utf-8 -*-
'''synchronized filtering linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.chains import ChainLinkMixin

__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


class collectchain(ChainLinkMixin, AutoQMixin, CollectMixin):

    '''synchronized collecting linked chain'''


class setchain(ChainLinkMixin, AutoQMixin, SetMixin):

    '''synchronized seting linked chain'''


class slicechain(ChainLinkMixin, AutoQMixin, SliceMixin):

    '''synchronized slicing linked chain'''


class filterchain(ChainLinkMixin, AutoQMixin, FilterMixin):

    '''synchronized filtering linked chain'''
