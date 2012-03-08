# -*- coding: utf-8 -*-
'''active linked call chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoQMixin, ManQMixin

from callchain.keys.queue import KQueue
from callchain.chains import RootedMixin
from callchain.octopus import Tentacle, Octuplet
from callchain.keys.chain import KChainLink, KEventLink

from callchain.events import ERootedMixin, EventMixin
from callchain.active.mixins import (
    ActiveMixin, ActiveRootedMixin, ActiveEMixin, RootMixin)

###############################################################################
## mixins #####################################################################
###############################################################################


class ActiveLinkMixin(ActiveRootedMixin, ActiveMixin, Tentacle):

    '''active queued linked call chain mixin'''


class ActiveELinkMixin(ActiveEMixin, ERootedMixin, ActiveLinkMixin):

    '''active linked event chain mixin'''


class ActiveChainletMixin(ActiveRootedMixin, Octuplet):

    '''active queued chainlet mixin'''


class ActiveEventletMixin(EventMixin, ERootedMixin, ActiveChainletMixin):

    '''active eventlet mixin'''


###############################################################################
## root rooted chains #########################################################
###############################################################################


class chainlet(RootedMixin, RootMixin, Octuplet):

    '''root chainlets'''


class chainlink(RootMixin, RootedMixin, ActiveMixin, Tentacle):

    '''root linked chain'''


class eventlet(ERootedMixin, chainlet):

    '''root event chainlet'''


class eventlink(ERootedMixin, ActiveEMixin, chainlink):

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
