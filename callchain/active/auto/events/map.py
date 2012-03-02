# -*- coding: utf-8 -*-
'''auto-balancing mapping linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.active.events import AEventLinkMixin
from callchain.services.map import KDelay, KCopy, KRepeat, KMap

__all__ = ('delayevent', 'copyevent', 'repeatevent', 'mapevent')


@appifies(KDelay)
class delayevent(AEventLinkMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping linked event chain'''


@appifies(KCopy)
class copyevent(AEventLinkMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy linked event chain'''


@appifies(KRepeat)
class repeatevent(AEventLinkMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat linked event chain'''


@appifies(KMap)
class mapevent(AEventLinkMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping linked event chain'''
