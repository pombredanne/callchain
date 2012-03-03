# -*- coding: utf-8 -*-
'''synchronized mapping linked chains'''

from twoq.active.mixins import SyncQMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.active.chains import ChainLinkMixin

__all__ = ('delaychain', 'copychain', 'repeatchain', 'mapchain')


class delaychain(ChainLinkMixin, SyncQMixin, DelayMixin):

    '''synchronized delayed mapping linked chain'''


class copychain(ChainLinkMixin, SyncQMixin, CopyMixin):

    '''synchronized copy linked chain'''


class repeatchain(ChainLinkMixin, SyncQMixin, RepeatMixin):

    '''synchronized repeat linked chain'''


class mapchain(ChainLinkMixin, SyncQMixin, MapMixin):

    '''synchronized mapping linked chain'''
