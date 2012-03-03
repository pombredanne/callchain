# -*- coding: utf-8 -*-
'''active auto-balancing event chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, AutoResultMixin

from callchain.active.auto.events.apps import autoevent
from callchain.events.keys import KEventLink, KEventChain
from callchain.active.events import EventLinkMixin, EventChainMixin

__all__ = ['eventlink', 'eventchain']


@appifies(KEventLink)
class eventlink(EventLinkMixin, AutoQMixin):

    '''auto-balancing linked event chain'''


@appifies(KEventChain)
@inside(autoevent)
class eventchain(EventChainMixin, AutoResultMixin):

    '''auto-balancing event chain'''
