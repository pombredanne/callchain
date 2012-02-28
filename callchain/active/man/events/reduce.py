# -*- coding: utf-8 -*-
'''manually balanced reducing linked event events'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.mixins.events import AEventLinkMixin

__all__ = ('mathevent', 'truthevent', 'reduceevent')


class mathevent(AEventLinkMixin, AutoQMixin, MathMixin):

    '''manually balanced mathing linked event event'''


class reduceevent(AEventLinkMixin, AutoQMixin, ReduceMixin):

    '''manually balanced reducing linked event event'''


class truthevent(AEventLinkMixin, AutoQMixin, TruthMixin):

    '''manually balanced truthing linked event event'''
