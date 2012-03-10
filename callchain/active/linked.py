# -*- coding: utf-8 -*-
'''active queued linked call chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, ManQMixin

from callchain.keys.queue import KQueue
from callchain.keys.chain import KChainLink, KEventLink
from callchain.assembly.linked import LinkedQ, EventlinkQ


@appifies(KChainLink, KQueue)
class aalinkq(LinkedQ, AutoQMixin):

    '''active queued auto-balancing linked call chain'''


@appifies(KChainLink, KQueue)
class amlinkq(LinkedQ, ManQMixin):

    '''active queued manually balanced linked call chain'''


@appifies(KEventLink, KQueue)
class aaelinkq(EventlinkQ, AutoQMixin):

    '''active queued auto-balancing linked event chain'''


@appifies(KEventLink, KQueue)
class amelinkq(EventlinkQ, ManQMixin):

    '''active queued manually balanced linked event chain'''
