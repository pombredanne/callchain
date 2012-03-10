# -*- coding: utf-8 -*-
'''active queued linked call chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, ManQMixin

from callchain.keys.queue import KQueue
from callchain.keys.chain import KChainLink, KEventLink
from callchain.assembly.linked import LinkedQ, EventlinkQ

from callchain.mixins.active import (
    ActiveCallMixin, ActiveECallMixin, ActiveRootedMixin)


class ActiveLinkMixin(LinkedQ, ActiveRootedMixin, ActiveCallMixin):

    '''active queued linked call chain mixin'''


@appifies(KChainLink, KQueue)
class aalinkq(ActiveLinkMixin, AutoQMixin):

    '''active queued auto-balancing linked call chain'''


@appifies(KChainLink, KQueue)
class amlinkq(ActiveLinkMixin, ManQMixin):

    '''active queued manually balanced linked call chain'''


class ActiveELinkMixin(EventlinkQ, ActiveRootedMixin, ActiveECallMixin):

    '''active queued linked event chain mixin'''


@appifies(KEventLink, KQueue)
class aaelinkq(ActiveELinkMixin, AutoQMixin):

    '''active queued auto-balancing linked event chain'''


@appifies(KEventLink, KQueue)
class amelinkq(ActiveELinkMixin, ManQMixin):

    '''active queued manually balanced linked event chain'''
