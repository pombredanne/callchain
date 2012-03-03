# -*- coding: utf-8 -*-
'''manually balanced reducing linked event events'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.events import LinkMixin
from callchain.services.reduce import KMath, KReduce, KTruth

__all__ = ('mathevent', 'truthevent', 'reduceevent')


@appifies(KMath)
class mathevent(LinkMixin, ManQMixin, MathMixin):

    '''manually balanced mathing linked event event'''


@appifies(KReduce)
class reduceevent(LinkMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing linked event event'''


@appifies(KTruth)
class truthevent(LinkMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing linked event event'''
