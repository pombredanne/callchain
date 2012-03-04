# -*- coding: utf-8 -*-
'''manually balanced reducing linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.chains.services.reduce import KMath, KReduce, KTruth

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('mathchain', 'truthchain', 'reducechain')


@appifies(KMath)
class mathchain(EventLinkMixin, ManQMixin, MathMixin):

    '''manually balanced mathing linked chain'''


@appifies(KReduce)
class reducechain(EventLinkMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing linked chain'''


@appifies(KTruth)
class truthchain(EventLinkMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing linked chain'''
