# -*- coding: utf-8 -*-
'''synchronized reducing linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.chains import AChainLinkMixin

__all__ = ('mathchain', 'truthchain', 'reducechain')


class mathchain(AChainLinkMixin, AutoQMixin, MathMixin):

    '''synchronized mathing linked chain'''


class reducechain(AChainLinkMixin, AutoQMixin, ReduceMixin):

    '''synchronized reducing linked chain'''


class truthchain(AChainLinkMixin, AutoQMixin, TruthMixin):

    '''synchronized truthing linked chain'''
