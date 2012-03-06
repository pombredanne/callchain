# -*- coding: utf-8 -*-
'''lazy auto-balancing call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin, AutoResultMixin

from callchain.octopus import inside

from callchain.chains.autolazy.apps import chain
from callchain.chains.keys.queue import KQueue, KResults
from callchain.chains.keys.core import KChainLink, KCallChain
from callchain.chains.queue import LazyLinkMixin, LazyChainMixin

__all__ = ('chainq', 'linkq')


@appifies(KChainLink, KQueue)
class linkq(LazyLinkMixin, AutoQMixin):

    '''auto-balancing linked call chain'''


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(LazyChainMixin, AutoResultMixin):

    '''auto-balancing call chain'''
