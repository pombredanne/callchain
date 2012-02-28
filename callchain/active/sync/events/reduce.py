# -*- coding: utf-8 -*-
'''synchronized reducing linked event events'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.mixins.events import AEventLinkMixin

__all__ = ('mathevent', 'truthevent', 'reduceevent')


class mathevent(AEventLinkMixin, AutoQMixin, MathMixin):

    '''synchronized mathing linked event event'''


class reduceevent(AEventLinkMixin, AutoQMixin, ReduceMixin):

    '''synchronized reducing linked event event'''


class truthevent(AEventLinkMixin, AutoQMixin, TruthMixin):

    '''synchronized truthing linked event event'''
