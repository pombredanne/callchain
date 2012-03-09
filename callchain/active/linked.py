# -*- coding: utf-8 -*-
'''active linked call chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, ManQMixin

from callchain.keys.queue import KQueue
from callchain.keys.chain import KChainLink, KEventLink
from callchain.linked import (
    Linked, ELinkedMixin, LinkedQMixin, LinkedChainMixin)

from callchain.active.chain import ActiveMixin
from callchain.active.chainlet import ActiveChainletMixin
from callchain.active.mixins import ActiveEMixin, RootMixin

###############################################################################
## mixins #####################################################################
###############################################################################


class ActiveLinkMixin(ActiveChainletMixin, ActiveMixin, LinkedQMixin):

    '''active queued linked call chain mixin'''


class ActiveELinkMixin(ActiveLinkMixin, ActiveEMixin, ELinkedMixin):

    '''active linked event chain mixin'''


###############################################################################
## root rooted chains #########################################################
###############################################################################


class chainlink(RootMixin, LinkedChainMixin, ActiveMixin, Linked):

    '''root linked chain'''


class eventlink(ActiveEMixin, ELinkedMixin, chainlink):

    '''root linked event chain'''


###############################################################################
## active queued chains #######################################################
###############################################################################


@appifies(KChainLink, KQueue)
class amlinkq(ActiveLinkMixin, ManQMixin):

    '''active manually balanced linked call chain'''


@appifies(KChainLink, KQueue)
class aalinkq(ActiveLinkMixin, AutoQMixin):

    '''active auto-balancing linked call chain'''


@appifies(KEventLink, KQueue)
class aaelinkq(ActiveELinkMixin, AutoQMixin):

    '''active auto-balancing linked event chain'''


@appifies(KEventLink, KQueue)
class amelinkq(ActiveELinkMixin, ManQMixin):

    '''active manually balanced linked event chain'''
