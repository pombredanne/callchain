# -*- coding: utf-8 -*-
'''manually balanced mapping linked chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.active.chains import ChainLinkMixin
from callchain.services.map import KDelay, KCopy, KRepeat, KMap

__all__ = ('delaychain', 'copychain', 'repeatchain', 'mapchain')


@appifies(KDelay)
class delaychain(ChainLinkMixin, AutoQMixin, DelayMixin):

    '''manually balanced delayed mapping linked chain'''


@appifies(KCopy)
class copychain(ChainLinkMixin, AutoQMixin, CopyMixin):

    '''manually balanced copy linked chain'''


@appifies(KRepeat)
class repeatchain(ChainLinkMixin, AutoQMixin, RepeatMixin):

    '''manually balanced repeat linked chain'''


@appifies(KMap)
class mapchain(ChainLinkMixin, AutoQMixin, MapMixin):

    '''manually balanced mapping linked chain'''
