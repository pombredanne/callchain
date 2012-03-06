# -*- coding: utf-8 -*-
'''lazy auto-balancing call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin, AutoResultMixin

from callchain.octopus import inside

from callchain.chains.autolazy.apps import chain
from callchain.chains.chain import LazyChainQMixin
from callchain.chains.linked import LazyLinkQMixin
from callchain.chains.keys.queue import KQueue, KResults
from callchain.chains.keys.core import KChainLink, KCallChain

__all__ = ('chainq', 'linkedq')


@appifies(KChainLink, KQueue)
class linkedq(LazyLinkQMixin, AutoQMixin):

    '''auto-balancing linked call chain'''


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(LazyChainQMixin, AutoResultMixin):

    '''auto-balancing call chain'''
