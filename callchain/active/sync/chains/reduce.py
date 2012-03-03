# -*- coding: utf-8 -*-
'''synchronized reducing linked chains'''

from twoq.active.mixins import SyncQMixin
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from callchain.active.chains import ChainLinkMixin

__all__ = ('mathchain', 'truthchain', 'reducechain')


class mathchain(ChainLinkMixin, SyncQMixin, MathMixin):

    '''synchronized mathing linked chain'''


class reducechain(ChainLinkMixin, SyncQMixin, ReduceMixin):

    '''synchronized reducing linked chain'''


class truthchain(ChainLinkMixin, SyncQMixin, TruthMixin):

    '''synchronized truthing linked chain'''
