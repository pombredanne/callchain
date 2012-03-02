# -*- coding: utf-8 -*-
'''auto-balancing mapping linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.active.chains import AChainLinkMixin
from callchain.services.map import KDelay, KCopy, KRepeat, KMap

__all__ = ('delaychain', 'copychain', 'repeatchain', 'mapchain')


@appifies(KDelay)
class delaychain(AChainLinkMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping linked chain'''


@appifies(KCopy)
class copychain(AChainLinkMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy linked chain'''


@appifies(KRepeat)
class repeatchain(AChainLinkMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat linked chain'''


@appifies(KMap)
class mapchain(AChainLinkMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping linked chain'''
