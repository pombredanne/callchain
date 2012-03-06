# -*- coding: utf-8 -*-
'''active auto-balancing call chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, AutoResultMixin

from callchain.octopus import inside

from callchain.chains.autoactive.apps import chain
from callchain.chains.chain import ActiveChainQMixin
from callchain.chains.linked import ActiveLinkedQMixin
from callchain.chains.keys.queue import KQueue, KResults
from callchain.chains.keys.core import KChainLink, KCallChain

__all__ = ('chainq', 'linkedq')


@appifies(KChainLink, KQueue)
class linkedq(ActiveLinkedQMixin, AutoQMixin):

    '''auto-balancing linked call chain'''


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(ActiveChainQMixin, AutoResultMixin):

    '''auto-balancing call chain'''
