# -*- coding: utf-8 -*-
'''active auto-balancing call chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin

from callchain.chains.keys.queue import KQueue
from callchain.chains.keys.core import KChainLink
from callchain.chains.linked import ActiveLinkQMixin

__all__ = ['linkq']


@appifies(KChainLink, KQueue)
class linkq(ActiveLinkQMixin, AutoQMixin):

    '''active sauto-balancing linked call chain'''
