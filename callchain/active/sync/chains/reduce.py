# -*- coding: utf-8 -*-
'''synchronized reducing linked chains'''

from twoq.active.mixins import AutoQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.chains import ChainLinkMixin

__all__ = ('mathchain', 'truthchain', 'reducechain')


class mathchain(ChainLinkMixin, AutoQMixin, MathMixin):

    '''synchronized mathing linked chain'''


class reducechain(ChainLinkMixin, AutoQMixin, ReduceMixin):

    '''synchronized reducing linked chain'''


class truthchain(ChainLinkMixin, AutoQMixin, TruthMixin):

    '''synchronized truthing linked chain'''
