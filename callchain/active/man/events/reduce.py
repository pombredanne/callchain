# -*- coding: utf-8 -*-
'''manually balanced reducing linked event events'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.events import AEventLinkMixin
from callchain.services.reduce import KMath, KReduce, KTruth

__all__ = ('mathevent', 'truthevent', 'reduceevent')


@appifies(KMath)
class mathevent(AEventLinkMixin, AutoQMixin, MathMixin):

    '''manually balanced mathing linked event event'''


@appifies(KReduce)
class reduceevent(AEventLinkMixin, AutoQMixin, ReduceMixin):

    '''manually balanced reducing linked event event'''


@appifies(KTruth)
class truthevent(AEventLinkMixin, AutoQMixin, TruthMixin):

    '''manually balanced truthing linked event event'''
