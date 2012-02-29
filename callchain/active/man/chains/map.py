# -*- coding: utf-8 -*-
'''manually balanced mapping linked chains'''

from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from twoq.active.mixins import AutoQMixin

from callchain.active.chains import AChainLinkMixin

__all__ = ('delaychain', 'copychain', 'repeatchain', 'mapchain')


class delaychain(AChainLinkMixin, AutoQMixin, DelayMixin):

    '''manually balanced delayed mapping linked chain'''


class copychain(AChainLinkMixin, AutoQMixin, CopyMixin):

    '''manually balanced copy linked chain'''


class repeatchain(AChainLinkMixin, AutoQMixin, RepeatMixin):

    '''manually balanced repeat linked chain'''


class mapchain(AChainLinkMixin, AutoQMixin, MapMixin):

    '''manually balanced mapping linked chain'''
