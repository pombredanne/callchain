# -*- coding: utf-8 -*-
'''active manually balanced call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin

from callchain.active.man.chains.apps import manchain
from callchain.active.chains import AChainLinkMixin, ACallChainMixin
from callchain.chains.keys import KChainLink, KCallChain

__all__ = ('callchain', 'chainlink')


@appifies(KChainLink)
class chainlink(AChainLinkMixin, AutoQMixin):

    '''manually balanced linked call chain'''


@appifies(KCallChain)
@inside(manchain)
class callchain(ACallChainMixin, AutoQMixin):

    '''manually balanced call chain'''
