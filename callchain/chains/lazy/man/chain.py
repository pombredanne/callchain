# -*- coding: utf-8 -*-
'''lazy manually balanced call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin, ManResultMixin

from callchain.chains.lazy.man.apps import chain
from callchain.chains.keys import KChainLink, KCallChain
from callchain.chains.services.queue import KQueue, KResults
from callchain.chains.lazy.mixins import ChainLinkMixin, ChainMixin

__all__ = ('chainq', 'linkq')


@appifies(KChainLink, KQueue)
class linkq(ChainLinkMixin, ManQMixin):

    '''manually balanced linked call chain'''


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(ChainMixin, ManResultMixin):

    '''manually balanced call chain'''
