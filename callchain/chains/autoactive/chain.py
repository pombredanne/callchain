# -*- coding: utf-8 -*-
'''active auto-balancing call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, AutoResultMixin

from callchain.chains.autoactive.apps import chain
from callchain.chains.keys.queue import KQueue, KResults
from callchain.chains.keys.core import KChainLink, KCallChain
from callchain.chains.queue import ActiveLinkMixin, ActiveChainMixin

__all__ = ('chainq', 'linkq')


@appifies(KChainLink, KQueue)
class linkq(ActiveLinkMixin, AutoQMixin):

    '''auto-balancing linked call chain'''


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(ActiveChainMixin, AutoResultMixin):

    '''auto-balancing call chain'''
