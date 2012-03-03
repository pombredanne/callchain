# -*- coding: utf-8 -*-
'''synchronized filtering linked chains'''

from twoq.active.mixins import SyncQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.chains import ChainLinkMixin

__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


class collectchain(ChainLinkMixin, SyncQMixin, CollectMixin):

    '''synchronized collecting linked chain'''


class setchain(ChainLinkMixin, SyncQMixin, SetMixin):

    '''synchronized seting linked chain'''


class slicechain(ChainLinkMixin, SyncQMixin, SliceMixin):

    '''synchronized slicing linked chain'''


class filterchain(ChainLinkMixin, SyncQMixin, FilterMixin):

    '''synchronized filtering linked chain'''
