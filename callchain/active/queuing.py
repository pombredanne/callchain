# -*- coding: utf-8 -*-
'''active call chains'''

from twoq.mixins.mapping import MapMixin
from twoq.mixins.reducing import ReduceMixin
from twoq.mixins.ordering import OrderMixin
from twoq.mixins.filtering import FilterMixin

from twoq.active.mixins import AutoQMixin, ManQMixin, SyncQMixin

__all__ = ('achain', 'mchain', 'schain', 'callchain')


class achain(AutoQMixin, FilterMixin, MapMixin, ReduceMixin, OrderMixin):

    '''auto-balancing manipulation chain'''


class mchain(ManQMixin, FilterMixin, MapMixin, ReduceMixin, OrderMixin):

    '''manually balanced manipulation chain'''


class schain(SyncQMixin, FilterMixin, MapMixin, ReduceMixin, OrderMixin):

    '''autosyncing manipulation chain'''


callchain = achain
