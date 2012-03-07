# -*- coding: utf-8 -*-
'''lazy auto-balancing call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin

from callchain.chains.keys.queue import KQueue
from callchain.chains.keys.core import KChainLink
from callchain.chains.linked import LazyLinkQMixin

__all__ = ['linkq']


@appifies(KChainLink, KQueue)
class linkq(LazyLinkQMixin, AutoQMixin):

    '''lazy auto-balancing linked call chain'''
