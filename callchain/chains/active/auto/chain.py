# -*- coding: utf-8 -*-
'''active auto-balancing call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, AutoResultMixin

from callchain.chains.active.auto.apps import chain
from callchain.chains.keys import KChainLink, KCallChain
from callchain.chains.services.queue import KQueue, KResults
from callchain.chains.active.mixins import ChainLinkMixin, ChainMixin

__all__ = ('chainq', 'linkq')


@appifies(KChainLink, KQueue)
class linkq(ChainLinkMixin, AutoQMixin):

    '''auto-balancing linked call chain'''


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(ChainMixin, AutoResultMixin):

    '''auto-balancing call chain'''
