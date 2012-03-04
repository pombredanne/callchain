# -*- coding: utf-8 -*-
'''auto-balancing filtering linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.chains.services.filter import KCollect, KSet, KSlice, KFilter

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


@appifies(KCollect)
class collectchain(EventLinkMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked chain'''


@appifies(KSet)
class setchain(EventLinkMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked chain'''


@appifies(KSlice)
class slicechain(EventLinkMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked chain'''


@appifies(KFilter)
class filterchain(EventLinkMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked chain'''
