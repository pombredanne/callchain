# -*- coding: utf-8 -*-
'''active manually balanced call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import ManQMixin, ManResultMixin

from callchain.chains.active.man.apps import chain
from callchain.chains.keys import KChainLink, KCallChain
from callchain.chains.active.mixins import ChainLinkMixin, CallChainMixin

__all__ = ('callchain', 'chainlink')


@appifies(KChainLink)
class chainlink(ChainLinkMixin, ManQMixin):

    '''manually balanced linked call chain'''


@appifies(KCallChain)
@inside(chain)
class callchain(CallChainMixin, ManResultMixin):

    '''manually balanced call chain'''
