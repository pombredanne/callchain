# -*- coding: utf-8 -*-
'''manually balanced filtering linked event chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from callchain.active.events import AEventLinkMixin

__all__ = ('collectevent', 'setevent', 'sliceevent', 'filterevent')


class collectevent(AEventLinkMixin, AutoQMixin, CollectMixin):

    '''manually balanced collecting linked event chain'''


class setevent(AEventLinkMixin, AutoQMixin, SetMixin):

    '''manually balanced seting linked event chain'''


class sliceevent(AEventLinkMixin, AutoQMixin, SliceMixin):

    '''manually balanced slicing linked event chain'''


class filterevent(AEventLinkMixin, AutoQMixin, FilterMixin):

    '''manually balanced filtering linked event chain'''
