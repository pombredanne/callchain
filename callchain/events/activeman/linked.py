# -*- coding: utf-8 -*-
'''active manually balanced event chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin

from callchain.chains.keys.queue import KQueue

from callchain.events.keys.core import KEventLink
from callchain.events.linked import ActiveELinkQMixin

__all__ = ['eventlink']


@appifies(KEventLink, KQueue)
class eventlink(ActiveELinkQMixin, ManQMixin):

    '''active manually balanced linked event chain'''
