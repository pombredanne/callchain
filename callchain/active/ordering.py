# -*- coding: utf-8 -*-
'''ordering linked active call chains'''

from inspect import ismodule

from twoq.support import port
from twoq.mixins.ordering import RandomMixin, OrderMixin

from twoq.active.mixins import AutoQMixin, ManQMixin, SyncQMixin

###############################################################################
## active random linked call chains ###########################################
###############################################################################


class arandomchain(AutoQMixin, RandomMixin):

    '''auto-balanced random linked call chain'''

randomchain = arandomchain


class mrandomchain(ManQMixin, RandomMixin):

    '''manually balanced random linked call chain'''


class srandomchain(SyncQMixin, RandomMixin):

    '''autosynchronized random linked call chain'''

###############################################################################
## active order linked call chains #####EEE####################################
###############################################################################


class aorderchain(AutoQMixin, OrderMixin):

    '''auto-balanced order linked call chain'''

orderchain = aorderchain


class morderchain(ManQMixin, OrderMixin):

    '''manually balanced order linked call chain'''


class sorderchain(SyncQMixin, OrderMixin):

    '''autosynchronized order linked call chain'''

__all__ = sorted(name for name, obj in port.items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
