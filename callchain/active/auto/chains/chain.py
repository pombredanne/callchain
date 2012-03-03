# -*- coding: utf-8 -*-
'''active auto-balancing call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, AutoMixin

from callchain.active.auto.chains.apps import autochain
from callchain.chains.keys import KChainLink, KCallChain
from callchain.active.chains import ChainLinkMixin, CallChainMixin

__all__ = ('callchain', 'chainlink')


@appifies(KChainLink)
class chainlink(ChainLinkMixin, AutoQMixin):

    '''auto-balancing linked call chain'''


@appifies(KCallChain)
@inside(autochain)
class callchain(CallChainMixin, AutoMixin):

    '''auto-balancing call chain'''
