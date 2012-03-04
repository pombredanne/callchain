# -*- coding: utf-8 -*-
'''manually balanced filtering linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.chains.active.mixins import ChainLinkMixin
from callchain.chains.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


@appifies(KCollect)
class collectchain(ChainLinkMixin, ManQMixin, CollectMixin):

    '''manually balanced collecting linked chain'''


@appifies(KSet)
class setchain(ChainLinkMixin, ManQMixin, SetMixin):

    '''manually balanced seting linked chain'''


@appifies(KSlice)
class slicechain(ChainLinkMixin, ManQMixin, SliceMixin):

    '''manually balanced slicing linked chain'''


@appifies(KFilter)
class filterchain(ChainLinkMixin, ManQMixin, FilterMixin):

    '''manually balanced filtering linked chain'''
