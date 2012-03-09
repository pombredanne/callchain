# -*- coding: utf-8 -*-
'''lazy queued linked call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin, ManQMixin

from callchain.keys.queue import KQueue
from callchain.linked import LinkedQMixin, ELinkedMixin
from callchain.keys.chain import KChainLink, KEventLink

from callchain.lazy.chainlet import LazyChainletMixin
from callchain.lazy.mixins import LazyMixin, LazyEMixin


class LazyLinkMixin(LazyChainletMixin, LazyMixin, LinkedQMixin):

    '''lazy queued linked call chain mixin'''


class LazyELinkMixin(LazyLinkMixin, LazyEMixin,  ELinkedMixin):

    '''lazy queued linked event chain mixin'''


@appifies(KChainLink, KQueue)
class lalinkq(LazyLinkMixin, AutoQMixin):

    '''lazy queued auto-balancing linked call chain'''


@appifies(KChainLink, KQueue)
class lmlinkq(LazyLinkMixin, ManQMixin):

    '''lazy queued manually balanced linked call chain'''


@appifies(KEventLink, KQueue)
class laelinkq(LazyELinkMixin, AutoQMixin):

    '''lazy queued auto-balancing linked event chain'''


@appifies(KEventLink, KQueue)
class lmelinkq(LazyELinkMixin, ManQMixin):

    '''lazy queued manually balanced linked event chain'''
