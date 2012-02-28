# -*- coding: utf-8 -*-
'''synchronized filtering linked event chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.mixins.events import AEventLinkMixin

__all__ = ('collectevent', 'setevent', 'sliceevent', 'filterevent')


class collectevent(AEventLinkMixin, AutoQMixin, CollectMixin):

    '''synchronized collecting linked event chain'''


class setevent(AEventLinkMixin, AutoQMixin, SetMixin):

    '''synchronized seting linked event chain'''


class sliceevent(AEventLinkMixin, AutoQMixin, SliceMixin):

    '''synchronized slicing linked event chain'''


class filterevent(AEventLinkMixin, AutoQMixin, FilterMixin):

    '''synchronized filtering linked event chain'''
