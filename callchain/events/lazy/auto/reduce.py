# -*- coding: utf-8 -*-
'''auto-balancing reducing linked event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.chains.services.reduce import KMath, KReduce, KTruth

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('mathchain', 'truthchain', 'reducechain')


@appifies(KMath)
class mathevent(EventLinkMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing linked event chains'''


@appifies(KReduce)
class reduceevent(EventLinkMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing linked event chains'''


@appifies(KTruth)
class truthevent(EventLinkMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing linked event chains'''
