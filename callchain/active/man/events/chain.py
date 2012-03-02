# -*- coding: utf-8 -*-
'''active manually balanced event chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin

from callchain.active.man.events.apps import manevent
from callchain.active.events import AEventLinkMixin, AEventChainMixin
from callchain.events.keys import KEventLink, KEventChain

__all__ = ['eventlink', 'eventchain']


@appifies(KEventLink)
class eventlink(AEventLinkMixin, AutoQMixin):

    '''manually balanced linked event chain'''


@appifies(KEventChain)
@inside(manevent)
class eventchain(AEventChainMixin, AutoQMixin):

    '''manually balanced event chain'''
