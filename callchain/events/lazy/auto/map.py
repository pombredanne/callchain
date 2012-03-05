# -*- coding: utf-8 -*-
'''auto-balancing mapping linked event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.chains.services.map import KDelay, KCopy, KRepeat, KMap

from callchain.events.lazy.mixins import EventLinkMixin

__all__ = ('delaychain', 'copychain', 'repeatchain', 'mapchain')


@appifies(KDelay)
class delayevent(EventLinkMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping linked event chain'''


@appifies(KCopy)
class copyevent(EventLinkMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy linked event chain'''


@appifies(KRepeat)
class repeatevent(EventLinkMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat linked event chain'''


@appifies(KMap)
class mapevent(EventLinkMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping linked event chain'''
