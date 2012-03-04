# -*- coding: utf-8 -*-
'''manually balanced reducing linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.chains.lazy.mixins import ChainLinkMixin
from callchain.chains.services.reduce import KMath, KReduce, KTruth

__all__ = ('mathchain', 'truthchain', 'reducechain')


@appifies(KMath)
class mathchain(ChainLinkMixin, ManQMixin, MathMixin):

    '''manually balanced mathing linked chain'''


@appifies(KReduce)
class reducechain(ChainLinkMixin, ManQMixin, ReduceMixin):

    '''manually balanced reducing linked chain'''


@appifies(KTruth)
class truthchain(ChainLinkMixin, ManQMixin, TruthMixin):

    '''manually balanced truthing linked chain'''
