# -*- coding: utf-8 -*-
'''auto-balancing reducing linked event events'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.mixins.events import AEventLinkMixin

__all__ = ('mathevent', 'truthevent', 'reduceevent')


class mathevent(AEventLinkMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing linked event event'''


class reduceevent(AEventLinkMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing linked event event'''


class truthevent(AEventLinkMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing linked event event'''
