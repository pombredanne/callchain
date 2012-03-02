# -*- coding: utf-8 -*-
'''auto-balancing filtering linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.chains import AChainLinkMixin
from callchain.services.filter import KCollect, KSet, KSlice, KFilter


__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


@appifies(KCollect)
class collectchain(AChainLinkMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked chain'''


@appifies(KSet)
class setchain(AChainLinkMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked chain'''


@appifies(KSlice)
class slicechain(AChainLinkMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked chain'''


@appifies(KFilter)
class filterchain(AChainLinkMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked chain'''
