# -*- coding: utf-8 -*-
'''manually balanced mapping linked event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from callchain.active.events import AEventLinkMixin
from callchain.services.map import KDelay, KCopy, KRepeat, KMap

__all__ = ('delayevent', 'copyevent', 'repeatevent', 'mapevent')


@appifies(KDelay)
class delayevent(AEventLinkMixin, AutoQMixin, DelayMixin):

    '''manually balanced delayed mapping linked event chain'''


@appifies(KCopy)
class copyevent(AEventLinkMixin, AutoQMixin, CopyMixin):

    '''manually balanced copy linked event chain'''


@appifies(KRepeat)
class repeatevent(AEventLinkMixin, AutoQMixin, RepeatMixin):

    '''manually balanced repeat linked event chain'''


@appifies(KMap)
class mapevent(AEventLinkMixin, AutoQMixin, MapMixin):

    '''manually balanced mapping linked event chain'''
