# -*- coding: utf-8 -*-
'''auto-balancing filtering linked event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.chains.services.filter import KCollect, KSet, KSlice, KFilter

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('collectevent', 'setevent', 'sliceevent', 'filterevent')


@appifies(KCollect)
class collectevent(EventLinkMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked event chain'''


@appifies(KSet)
class setevent(EventLinkMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked event chain'''


@appifies(KSlice)
class sliceevent(EventLinkMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked event chain'''


@appifies(KFilter)
class filterevent(EventLinkMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked event chain'''
