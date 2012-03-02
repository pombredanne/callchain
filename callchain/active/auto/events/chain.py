# -*- coding: utf-8 -*-
'''active auto-balancing event chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin

from callchain.active.auto.events.apps import autoevent
from callchain.active.events import AEventLinkMixin, AEventChainMixin
from callchain.events.keys import KEventLink, KEventChain

__all__ = ['eventlink', 'eventchain']


@appifies(KEventLink)
class eventlink(AEventLinkMixin, AutoQMixin):

    '''auto-balancing linked event chain'''


@appifies(KEventChain)
@inside(autoevent)
class eventchain(AEventChainMixin, AutoQMixin):

    '''auto-balancing event chain'''
