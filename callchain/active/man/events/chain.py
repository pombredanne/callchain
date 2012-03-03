# -*- coding: utf-8 -*-
'''active manually balanced event chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, AutoMixin

from callchain.active.man.events.apps import manevent
from callchain.events.keys import KEventLink, KEventChain
from callchain.active.events import EventLinkMixin, EventChainMixin

__all__ = ['eventlink', 'eventchain']


@appifies(KEventLink)
class eventlink(EventLinkMixin, AutoQMixin):

    '''manually balanced linked event chain'''


@appifies(KEventChain)
@inside(manevent)
class eventchain(EventChainMixin, AutoMixin):

    '''manually balanced event chain'''
