# -*- coding: utf-8 -*-
'''active manually balanced call chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManQMixin, ManResultMixin

from callchain.octopus import inside

from callchain.chains.activeman.apps import chain
from callchain.chains.keys.queue import KQueue, KResults
from callchain.chains.keys.core import KChainLink, KCallChain
from callchain.chains.queue import ActiveLinkMixin, ActiveChainMixin

__all__ = ('chainq', 'linkq')


@appifies(KChainLink, KQueue)
class linkq(ActiveLinkMixin, ManQMixin):

    '''manually balanced linked call chain'''


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(ActiveChainMixin, ManResultMixin):

    '''manually balanced call chain'''
