# -*- coding: utf-8 -*-
'''lazy auto-balancing call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoResultMixin

from callchain.octopus import inside

from callchain.chains.keys.queue import KResults
from callchain.chains.keys.core import KCallChain
from callchain.chains.chain import LazyChainQMixin

from callchain.chains.autolazy.apps import chain

__all__ = ['chainq']


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(LazyChainQMixin, AutoResultMixin):

    '''lazy auto-balancing call chain'''
