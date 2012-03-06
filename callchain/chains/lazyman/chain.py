# -*- coding: utf-8 -*-
'''lazy manually balanced call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManQMixin, ManResultMixin

from callchain.octopus import inside

from callchain.chains.lazyman.apps import chain
from callchain.chains.keys.queue import KQueue, KResults
from callchain.chains.keys.core import KChainLink, KCallChain
from callchain.chains.queue import LazyLinkMixin, LazyChainMixin

__all__ = ('chainq', 'linkq')


@appifies(KChainLink, KQueue)
class linkq(LazyLinkMixin, ManQMixin):

    '''manually balanced linked call chain'''


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(LazyChainMixin, ManResultMixin):

    '''manually balanced call chain'''
