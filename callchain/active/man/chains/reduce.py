# -*- coding: utf-8 -*-
'''manually balanced reducing linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.chains import AChainLinkMixin
from callchain.services.reduce import KMath, KReduce, KTruth

__all__ = ('mathchain', 'truthchain', 'reducechain')


@appifies(KMath)
class mathchain(AChainLinkMixin, AutoQMixin, MathMixin):

    '''manually balanced mathing linked chain'''


@appifies(KReduce)
class reducechain(AChainLinkMixin, AutoQMixin, ReduceMixin):

    '''manually balanced reducing linked chain'''


@appifies(KTruth)
class truthchain(AChainLinkMixin, AutoQMixin, TruthMixin):

    '''manually balanced truthing linked chain'''
