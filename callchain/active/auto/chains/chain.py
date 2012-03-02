# -*- coding: utf-8 -*-
'''active auto-balancing call chains'''

from octopus import inside
from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin

from callchain.active.auto.chains.apps import autochain
from callchain.chains.keys import KChainLink, KCallChain
from callchain.active.chains import AChainLinkMixin, ACallChainMixin

__all__ = ('callchain', 'chainlink')


@appifies(KChainLink)
class chainlink(AChainLinkMixin, AutoQMixin):

    '''auto-balancing linked chain'''


@appifies(KCallChain)
@inside(autochain)
class callchain(ACallChainMixin, AutoQMixin):

    '''auto-balancing call chain'''
