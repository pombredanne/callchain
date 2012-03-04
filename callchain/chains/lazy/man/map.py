# -*- coding: utf-8 -*-
'''manually balanced mapping linked chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.lazy.mixins import ChainLinkMixin
from callchain.chains.services.map import KDelay, KCopy, KRepeat, KMap

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
