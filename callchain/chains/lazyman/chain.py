# -*- coding: utf-8 -*-
'''lazy manually balanced call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManResultMixin

from callchain.octopus import inside

from callchain.chains.keys.queue import KResults
from callchain.chains.keys.core import KCallChain
from callchain.chains.chain import LazyChainQMixin

from callchain.chains.lazyman.apps import chain

__all__ = ['chainq']


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(LazyChainQMixin, ManResultMixin):

    '''lazy manually balanced call chain'''
