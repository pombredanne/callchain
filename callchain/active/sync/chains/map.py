# -*- coding: utf-8 -*-
'''synchronized mapping linked chains'''

from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from twoq.active.mixins import AutoQMixin

from callchain.active.chains import AChainLinkMixin

__all__ = ('delaychain', 'copychain', 'repeatchain', 'mapchain')


class delaychain(AChainLinkMixin, AutoQMixin, DelayMixin):

    '''synchronized delayed mapping linked chain'''


class copychain(AChainLinkMixin, AutoQMixin, CopyMixin):

    '''synchronized copy linked chain'''


class repeatchain(AChainLinkMixin, AutoQMixin, RepeatMixin):

    '''synchronized repeat linked chain'''


class mapchain(AChainLinkMixin, AutoQMixin, MapMixin):

    '''synchronized mapping linked chain'''
