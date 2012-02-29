# -*- coding: utf-8 -*-
'''auto-balancing reducing linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.chains import AChainLinkMixin

__all__ = ('mathchain', 'truthchain', 'reducechain')


class mathchain(AChainLinkMixin, AutoQMixin, MathMixin):

    '''auto-balancing mathing linked chain'''


class reducechain(AChainLinkMixin, AutoQMixin, ReduceMixin):

    '''auto-balancing reducing linked chain'''


class truthchain(AChainLinkMixin, AutoQMixin, TruthMixin):

    '''auto-balancing truthing linked chain'''
