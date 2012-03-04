# -*- coding: utf-8 -*-
'''lazy manually balanced call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin, ManResultMixin

from callchain.chains.lazy.man.apps import chain
from callchain.chains.keys import KChainLink, KCallChain
from callchain.chains.lazy.mixins import ChainLinkMixin, CallChainMixin

__all__ = ('callchain', 'chainlink')


@appifies(KChainLink)
class chainlink(ChainLinkMixin, ManQMixin):

    '''manually balanced linked call chain'''


@appifies(KCallChain)
@inside(chain)
class callchain(CallChainMixin, ManResultMixin):

    '''manually balanced call chain'''
