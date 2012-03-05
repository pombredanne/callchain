# -*- coding: utf-8 -*-
'''manually balanced filtering linked event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.chains.services.filter import KCollect, KSet, KSlice, KFilter

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('collectevent', 'setevent', 'sliceevent', 'filterevent')


@appifies(KCollect)
class collectevent(EventLinkMixin, ManQMixin, CollectMixin):

    '''manually balanced collecting linked event chain'''


@appifies(KSet)
class setevent(EventLinkMixin, ManQMixin, SetMixin):

    '''manually balanced seting linked event chain'''


@appifies(KSlice)
class sliceevent(EventLinkMixin, ManQMixin, SliceMixin):

    '''manually balanced slicing linked event chain'''


@appifies(KFilter)
class filterevent(EventLinkMixin, ManQMixin, FilterMixin):

    '''manually balanced filtering linked event chain'''
