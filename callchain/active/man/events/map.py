# -*- coding: utf-8 -*-
'''manually balanced mapping linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.active.events import EventLinkMixin
from callchain.services.map import KDelay, KCopy, KRepeat, KMap

__all__ = ('delayevent', 'copyevent', 'repeatevent', 'mapevent')


@appifies(KDelay)
class delayevent(EventLinkMixin, ManQMixin, DelayMixin):

    '''manually balanced delayed mapping linked event chain'''


@appifies(KCopy)
class copyevent(EventLinkMixin, ManQMixin, CopyMixin):

    '''manually balanced copy linked event chain'''


@appifies(KRepeat)
class repeatevent(EventLinkMixin, ManQMixin, RepeatMixin):

    '''manually balanced repeat linked event chain'''


@appifies(KMap)
class mapevent(EventLinkMixin, ManQMixin, MapMixin):

    '''manually balanced mapping linked event chain'''
