# -*- coding: utf-8 -*-
'''manually balanced filtering linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.chains.services.filter import KCollect, KSet, KSlice, KFilter

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('collectchain', 'setchain', 'slicechain', 'filterchain')


@appifies(KCollect)
class collectchain(EventLinkMixin, ManQMixin, CollectMixin):

    '''manually balanced collecting linked chain'''


@appifies(KSet)
class setchain(EventLinkMixin, ManQMixin, SetMixin):

    '''manually balanced seting linked chain'''


@appifies(KSlice)
class slicechain(EventLinkMixin, ManQMixin, SliceMixin):

    '''manually balanced slicing linked chain'''


@appifies(KFilter)
class filterchain(EventLinkMixin, ManQMixin, FilterMixin):

    '''manually balanced filtering linked chain'''
