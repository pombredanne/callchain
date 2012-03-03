# -*- coding: utf-8 -*-
'''active manually balanced call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, AutoMixin

from callchain.active.man.chains.apps import manchain
from callchain.chains.keys import KChainLink, KCallChain
from callchain.active.chains import ChainLinkMixin, CallChainMixin

__all__ = ('callchain', 'chainlink')


@appifies(KChainLink)
class chainlink(ChainLinkMixin, AutoQMixin):

    '''manually balanced linked call chain'''


@appifies(KCallChain)
@inside(manchain)
class callchain(CallChainMixin, AutoMixin):

    '''manually balanced call chain'''
