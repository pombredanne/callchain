# -*- coding: utf-8 -*-
'''twoq active ordering linked event chains'''

from inspect import ismodule

from twoq.support import port
from twoq.mixins.ordering import RandomMixin, OrderMixin

from twoq.active.mixins import AutoQMixin, ManQMixin, SyncQMixin

###############################################################################
## active random linked event chains ##########################################
###############################################################################


class arandomlink(AutoQMixin, RandomMixin):

    '''auto-balanced random linked event chain'''

randomlink = arandomlink


class mrandomlink(ManQMixin, RandomMixin):

    '''manually balanced random linked event chain'''


class srandomlink(SyncQMixin, RandomMixin):

    '''autosynchronized random linked event chain'''

###############################################################################
## active order linked event chains #####EEE###################################
###############################################################################


class aorderlink(AutoQMixin, OrderMixin):

    '''auto-balanced order linked event chain'''

orderlink = aorderlink


class morderlink(ManQMixin, OrderMixin):

    '''manually balanced order linked event chain'''


class sorderlink(SyncQMixin, OrderMixin):

    '''autosynchronized order linked event chain'''

__all__ = sorted(name for name, obj in port.items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
