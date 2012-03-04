# -*- coding: utf-8 -*-
'''auto-balancing filtering linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.chains.active.mixins import ChainLinkMixin
from callchain.chains.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


@appifies(KCollect)
class collectchain(ChainLinkMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked chain'''


@appifies(KSet)
class setchain(ChainLinkMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked chain'''


@appifies(KSlice)
class slicechain(ChainLinkMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked chain'''


@appifies(KFilter)
class filterchain(ChainLinkMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked chain'''
