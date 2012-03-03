# -*- coding: utf-8 -*-
'''synchronized reducing linked event events'''

from twoq.active.mixins import SyncQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.events import LinkMixin

__all__ = ('mathevent', 'truthevent', 'reduceevent')


class mathevent(LinkMixin, SyncQMixin, MathMixin):

    '''synchronized mathing linked event event'''


class reduceevent(LinkMixin, SyncQMixin, ReduceMixin):

    '''synchronized reducing linked event event'''


class truthevent(LinkMixin, SyncQMixin, TruthMixin):

    '''synchronized truthing linked event event'''
