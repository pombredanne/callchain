# -*- coding: utf-8 -*-
'''lazy queued linked call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin, ManQMixin

from callchain.keys.queue import KQueue
from callchain.keys.chain import KChainLink, KEventLink
from callchain.assembly.linked import LinkedQ, EventlinkQ

from callchain.lazy.mixins import (
    LazyCallMixin, LazyECallMixin, LazyRootedMixin)


class LazyLinkMixin(LinkedQ, LazyRootedMixin, LazyCallMixin):

    '''lazy queued linked call chain mixin'''


@appifies(KChainLink, KQueue)
class lalinkq(LazyLinkMixin, AutoQMixin):

    '''lazy queued auto-balancing linked call chain'''


@appifies(KChainLink, KQueue)
class lmlinkq(LazyLinkMixin, ManQMixin):

    '''lazy queued manually balanced linked call chain'''


class LazyELinkMixin(EventlinkQ, LazyRootedMixin, LazyECallMixin):

    '''lazy queued linked event chain mixin'''


@appifies(KEventLink, KQueue)
class laelinkq(LazyELinkMixin, AutoQMixin):

    '''lazy queued auto-balancing linked event chain'''


@appifies(KEventLink, KQueue)
class lmelinkq(LazyELinkMixin, ManQMixin):

    '''lazy queued manually balanced linked event chain'''
