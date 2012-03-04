# -*- coding: utf-8 -*-
'''auto-balancing reducing linked event events'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.chains.services.reduce import KMath, KReduce, KTruth

from callchain.events.active.mixins import EventLinkMixin

__all__ = ('mathevent', 'truthevent', 'reduceevent')


@appifies(KMath)
class mathevent(EventLinkMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing linked event event'''


@appifies(KReduce)
class reduceevent(EventLinkMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing linked event event'''


@appifies(KTruth)
class truthevent(EventLinkMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing linked event event'''
