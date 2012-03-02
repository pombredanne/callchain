# -*- coding: utf-8 -*-
'''auto-balancing filtering linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.events import AEventLinkMixin
from callchain.services.filter import KCollect, KSet, KSlice, KFilter

__all__ = ('collectevent', 'setevent', 'sliceevent', 'filterevent')


@appifies(KCollect)
class collectevent(AEventLinkMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked event chain'''


@appifies(KSet)
class setevent(AEventLinkMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked event chain'''


@appifies(KSlice)
class sliceevent(AEventLinkMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked event chain'''


@appifies(KFilter)
class filterevent(AEventLinkMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked event chain'''
