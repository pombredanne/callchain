# -*- coding: utf-8 -*-
'''auto-balancing mapping linked chains'''

from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from twoq.active.mixins import AutoQMixin

from callchain.active.mixins.chains import AChainLinkMixin

__all__ = ('delaychain', 'copychain', 'repeatchain', 'mapchain')


class delaychain(AChainLinkMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping linked chain'''


class copychain(AChainLinkMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy linked chain'''


class repeatchain(AChainLinkMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat linked chain'''


class mapchain(AChainLinkMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping linked chain'''
