# -*- coding: utf-8 -*-
'''auto-balancing filtering linked event chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.mixins.events import AEventLinkMixin

__all__ = ('collectevent', 'setevent', 'sliceevent', 'filterevent')


class collectevent(AEventLinkMixin, AutoQMixin, CollectMixin):

    '''auto-balancing collecting linked event chain'''


class setevent(AEventLinkMixin, AutoQMixin, SetMixin):

    '''auto-balancing seting linked event chain'''


class sliceevent(AEventLinkMixin, AutoQMixin, SliceMixin):

    '''auto-balancing slicing linked event chain'''


class filterevent(AEventLinkMixin, AutoQMixin, FilterMixin):

    '''auto-balancing filtering linked event chain'''
