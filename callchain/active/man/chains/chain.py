# -*- coding: utf-8 -*-
'''active manually balanced call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import ManQMixin, ManResultMixin

from callchain.active.man.chains.apps import manchain
from callchain.chains.keys import KChainLink, KCallChain
from callchain.active.chains import ChainLinkMixin, CallChainMixin

__all__ = ('callchain', 'chainlink')


@appifies(KChainLink)
class chainlink(ChainLinkMixin, ManQMixin):

    '''manually balanced linked call chain'''


@appifies(KCallChain)
@inside(manchain)
class callchain(CallChainMixin, ManResultMixin):

    '''manually balanced call chain'''
