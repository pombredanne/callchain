# -*- coding: utf-8 -*-
'''manually balanced reducing linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.chains import AChainLinkMixin

__all__ = ('mathchain', 'truthchain', 'reducechain')


class mathchain(AChainLinkMixin, AutoQMixin, MathMixin):

    '''manually balanced mathing linked chain'''


class reducechain(AChainLinkMixin, AutoQMixin, ReduceMixin):

    '''manually balanced reducing linked chain'''


class truthchain(AChainLinkMixin, AutoQMixin, TruthMixin):

    '''manually balanced truthing linked chain'''
