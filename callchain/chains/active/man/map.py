# -*- coding: utf-8 -*-
'''manually balanced mapping linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.services.map import KDelay, KCopy, KRepeat, KMap

from callchain.chains.active.mixins import ChainLinkMixin

__all__ = ('delaychain', 'copychain', 'repeatchain', 'mapchain')


@appifies(KDelay)
class delaychain(ChainLinkMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping linked chain'''


@appifies(KCopy)
class copychain(ChainLinkMixin, ManQMixin, CopyMixin):

    '''manually balanced copy linked chain'''


@appifies(KRepeat)
class repeatchain(ChainLinkMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat linked chain'''


@appifies(KMap)
class mapchain(ChainLinkMixin, ManQMixin, MapMixin):

    '''manually balanced mapping linked chain'''
