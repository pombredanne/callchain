# -*- coding: utf-8 -*-
'''active event chain'''

from twoq.mixins.mapping import MapMixin
from twoq.mixins.reducing import ReduceMixin
from twoq.mixins.ordering import OrderMixin
from twoq.mixins.filtering import FilterMixin

from twoq.active.mixins import AutoQMixin, ManQMixin, SyncQMixin

__all__ = ('aevent', 'mevent', 'sevent', 'event')


class aeventchain(AutoQMixin, FilterMixin, MapMixin, ReduceMixin, OrderMixin):

    '''auto-balancing manipulation queue'''


class meventchain(ManQMixin, FilterMixin, MapMixin, ReduceMixin, OrderMixin):

    '''manually balanced manipulation queue'''


class seventchain(SyncQMixin, FilterMixin, MapMixin, ReduceMixin, OrderMixin):

    '''autosyncing manipulation queue'''


eventchain = aeventchain
