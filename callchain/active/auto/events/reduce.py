# -*- coding: utf-8 -*-
'''auto-balancing reducing linked event events'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.events import LinkMixin
from callchain.services.reduce import KMath, KReduce, KTruth

__all__ = ('mathevent', 'truthevent', 'reduceevent')


@appifies(KMath)
class mathevent(LinkMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing linked event event'''


@appifies(KReduce)
class reduceevent(LinkMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing linked event event'''


@appifies(KTruth)
class truthevent(LinkMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing linked event event'''
