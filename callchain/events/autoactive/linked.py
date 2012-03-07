# -*- coding: utf-8 -*-
'''active auto-balancing event chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin

from callchain.chains.keys.queue import KQueue

from callchain.events.keys.core import KEventLink
from callchain.events.linked import ActiveELinkQMixin

__all__ = ['eventlink']


@appifies(KEventLink, KQueue)
class eventlink(ActiveELinkQMixin, AutoQMixin):

    '''active auto-balancing linked event chain'''
