# -*- coding: utf-8 -*-
'''synchronized filtering linked event chains'''

from twoq.active.mixins import SyncQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.events import LinkMixin

__all__ = ('collectevent', 'setevent', 'sliceevent', 'filterevent')


class collectevent(LinkMixin, SyncQMixin, CollectMixin):

    '''synchronized collecting linked event chain'''


class setevent(LinkMixin, SyncQMixin, SetMixin):

    '''synchronized seting linked event chain'''


class sliceevent(LinkMixin, SyncQMixin, SliceMixin):

    '''synchronized slicing linked event chain'''


class filterevent(LinkMixin, SyncQMixin, FilterMixin):

    '''synchronized filtering linked event chain'''
