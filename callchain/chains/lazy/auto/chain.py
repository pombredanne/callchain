# -*- coding: utf-8 -*-
'''lazy auto-balancing call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin, AutoResultMixin

from callchain.chains.keys import KChainLink, KCallChain

from callchain.chains.lazy.auto.apps import chain
from callchain.chains.lazy.mixins import ChainLinkMixin, CallChainMixin

__all__ = ('callchain', 'chainlink')


@appifies(KChainLink)
class chainlink(ChainLinkMixin, AutoQMixin):

    '''auto-balancing linked call chain'''


@appifies(KCallChain)
@inside(chain)
class callchain(CallChainMixin, AutoResultMixin):

    '''auto-balancing call chain'''
