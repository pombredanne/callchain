# -*- coding: utf-8 -*-
'''manually balanced filtering linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.chains import ChainLinkMixin
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


@appifies(KCollect)
class collectchain(ChainLinkMixin, AutoQMixin, CollectMixin):

    '''manually balanced collecting linked chain'''


@appifies(KSet)
class setchain(ChainLinkMixin, AutoQMixin, SetMixin):

    '''manually balanced seting linked chain'''


@appifies(KSlice)
class slicechain(ChainLinkMixin, AutoQMixin, SliceMixin):

    '''manually balanced slicing linked chain'''


@appifies(KFilter)
class filterchain(ChainLinkMixin, AutoQMixin, FilterMixin):

    '''manually balanced filtering linked chain'''
