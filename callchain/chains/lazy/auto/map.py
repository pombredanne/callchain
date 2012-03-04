# -*- coding: utf-8 -*-
'''auto-balancing mapping linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.lazy.mixins import ChainLinkMixin
from callchain.chains.services.map import KDelay, KCopy, KRepeat, KMap

__all__ = ('delaychain', 'copychain', 'repeatchain', 'mapchain')


@appifies(KDelay)
class delaychain(ChainLinkMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping linked chain'''


@appifies(KCopy)
class copychain(ChainLinkMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy linked chain'''


@appifies(KRepeat)
class repeatchain(ChainLinkMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat linked chain'''


@appifies(KMap)
class mapchain(ChainLinkMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping linked chain'''
