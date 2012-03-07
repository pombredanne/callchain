# -*- coding: utf-8 -*-
'''active manually balanced call chains'''

from appspace.keys import appifies
from twoq.active.mixins import ManResultMixin

from callchain.octopus import inside

from callchain.chains.keys.queue import KResults
from callchain.chains.keys.core import KCallChain
from callchain.chains.chain import ActiveChainQMixin

from callchain.chains.activeman.apps import chain

__all__ = ['chainq']


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(ActiveChainQMixin, ManResultMixin):

    '''manually balanced call chain'''
