# -*- coding: utf-8 -*-
'''lazy auto-balancing event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin

from callchain.chains.keys.queue import KQueue

from callchain.events.keys.core import KEventLink
from callchain.events.chainlet import LazyELetQMixin

__all__ = ['eventlink']


@appifies(KEventLink, KQueue)
class eventlink(LazyELetQMixin, AutoQMixin):

    '''lazy auto-balancing linked event chain'''
