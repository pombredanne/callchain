# -*- coding: utf-8 -*-
'''lazy manually balanced event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin

from callchain.chains.keys.queue import KQueue

from callchain.events.keys.core import KEventLink
from callchain.events.chainlet import LazyELetQMixin

__all__ = ('eventchain', 'eventlink')


@appifies(KEventLink, KQueue)
class eventlink(LazyELetQMixin, ManQMixin):

    '''lazy manually balanced linked event chain'''
