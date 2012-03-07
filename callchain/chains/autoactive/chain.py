# -*- coding: utf-8 -*-
'''active auto-balancing call chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoResultMixin

from callchain.octopus import inside

from callchain.chains.keys.queue import KResults
from callchain.chains.keys.core import KCallChain
from callchain.chains.chain import ActiveChainQMixin

from callchain.chains.autoactive.apps import chain

__all__ = ['chainq']


@appifies(KCallChain, KResults)
@inside(chain)
class chainq(ActiveChainQMixin, AutoResultMixin):

    '''active sauto-balancing call chain'''
