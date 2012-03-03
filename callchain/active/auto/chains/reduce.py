# -*- coding: utf-8 -*-
'''auto-balancing reducing linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.services.reduce import KMath, KReduce, KTruth
from callchain.active.chains import ChainLinkMixin

__all__ = ('mathchain', 'truthchain', 'reducechain')


@appifies(KMath)
class mathchain(ChainLinkMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing linked chain'''


@appifies(KReduce)
class reducechain(ChainLinkMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing linked chain'''


@appifies(KTruth)
class truthchain(ChainLinkMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing linked chain'''
