# -*- coding: utf-8 -*-
'''manually balanced filtering linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.mixins.chains import AChainLinkMixin

__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


class collectchain(AChainLinkMixin, AutoQMixin, CollectMixin):

    '''manually balanced collecting linked chain'''


class setchain(AChainLinkMixin, AutoQMixin, SetMixin):

    '''manually balanced seting linked chain'''


class slicechain(AChainLinkMixin, AutoQMixin, SliceMixin):

    '''manually balanced slicing linked chain'''


class filterchain(AChainLinkMixin, AutoQMixin, FilterMixin):

    '''manually balanced filtering linked chain'''
