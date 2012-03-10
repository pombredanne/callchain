# -*- coding: utf-8 -*-
'''lazy queued linked call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoQMixin, ManQMixin

from callchain.keys.queue import KQueue
from callchain.keys.chain import KChainLink, KEventLink
from callchain.assembly.linked import LinkedQ, EventlinkQ


@appifies(KChainLink, KQueue)
class lalinkq(LinkedQ, AutoQMixin):

    '''lazy queued auto-balancing linked call chain'''


@appifies(KChainLink, KQueue)
class lmlinkq(LinkedQ, ManQMixin):

    '''lazy queued manually balanced linked call chain'''


@appifies(KEventLink, KQueue)
class laelinkq(EventlinkQ, AutoQMixin):

    '''lazy queued auto-balancing linked event chain'''


@appifies(KEventLink, KQueue)
class lmelinkq(EventlinkQ, ManQMixin):

    '''lazy queued manually balanced linked event chain'''
