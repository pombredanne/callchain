# -*- coding: utf-8 -*-
'''lazy queued linked call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin, ManQMixin

from callchain.octopus import Tentacle
from callchain.keys.queue import KQueue
from callchain.events import ERootedMixin
from callchain.keys.chain import KChainLink, KEventLink

from callchain.lazy.mixins import (
    LazyRootedMixin, LazyMixin, ELazyMixin, LazyEventletMixin)


class LazyLinkMixin(LazyRootedMixin, LazyMixin, Tentacle):

    '''lazy queued linked call chain mixin'''


class LazyELinkMixin(ELazyMixin, ERootedMixin, LazyLinkMixin):

    '''lazy queued linked event chain mixin'''


@appifies(KChainLink, KQueue)
class lalinkq(LazyLinkMixin, AutoQMixin):

    '''lazy queued auto-balancing linked call chain'''


@appifies(KChainLink, KQueue)
class lmlinkq(LazyLinkMixin, ManQMixin):

    '''lazy queued manually balanced linked call chain'''


@appifies(KEventLink, KQueue)
class laelinkq(LazyEventletMixin, AutoQMixin):

    '''lazy queued auto-balancing linked event chain'''


@appifies(KEventLink, KQueue)
class lmelinkq(LazyEventletMixin, ManQMixin):

    '''lazy queued manually balanced linked event chain'''
