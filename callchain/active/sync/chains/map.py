# -*- coding: utf-8 -*-
'''synchronized mapping linked chains'''

from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from twoq.active.mixins import AutoQMixin

from callchain.active.chains import ChainLinkMixin

__all__ = ('delaychain', 'copychain', 'repeatchain', 'mapchain')


class delaychain(ChainLinkMixin, AutoQMixin, DelayMixin):

    '''synchronized delayed mapping linked chain'''


class copychain(ChainLinkMixin, AutoQMixin, CopyMixin):

    '''synchronized copy linked chain'''


class repeatchain(ChainLinkMixin, AutoQMixin, RepeatMixin):

    '''synchronized repeat linked chain'''


class mapchain(ChainLinkMixin, AutoQMixin, MapMixin):

    '''synchronized mapping linked chain'''
