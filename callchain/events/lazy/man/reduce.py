# -*- coding: utf-8 -*-
'''manually balanced reducing linked event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.chains.services.reduce import KMath, KReduce, KTruth

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('mathevent', 'truthevent', 'reduceevent')


@appifies(KMath)
class mathevent(EventLinkMixin, ManQMixin, MathMixin):

    '''manually balanced mathing linked event chain'''


@appifies(KReduce)
class reduceevent(EventLinkMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing linked event chain'''


@appifies(KTruth)
class truthevent(EventLinkMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing linked event chain'''
