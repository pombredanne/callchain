# -*- coding: utf-8 -*-
'''active manually balanced call chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin, ManResultMixin

from callchain.octopus import inside

from callchain.chains.activeman.apps import chain
from callchain.chains.chain import ActiveChainQMixin
from callchain.chains.linked import ActiveLinkedQMixin
from callchain.chains.keys.queue import KQueue, KResults
from callchain.chains.keys.core import KChainLink, KCallChain

__all__ = ('chainq', 'linkedq')


@appifies(KChainLink, KQueue)
class linkedq(ActiveLinkedQMixin, ManQMixin):

    '''manually balanced linked call chain'''


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(ActiveChainQMixin, ManResultMixin):

    '''manually balanced call chain'''
