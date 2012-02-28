# -*- coding: utf-8 -*-
'''twoq active mapping linked event chain'''

from inspect import ismodule

from twoq.support import port
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from twoq.active.mixins import AutoQMixin, ManQMixin, SyncQMixin

###############################################################################
## active delayed map linked event chain ######################################
###############################################################################


class adelaylink(AutoQMixin, DelayMixin):

    '''auto-balanced delayed map linked event chain'''

delaylink = adelaylink


class mdelaylink(ManQMixin, DelayMixin):

    '''manually balanced delayed map linked event chain'''


class sdelaylink(SyncQMixin, DelayMixin):

    '''autosynchronized  delayed map linked event chain'''

###############################################################################
## active copy linked event chain #############################################
###############################################################################


class acopylink(AutoQMixin, CopyMixin):

    '''auto-balanced copy linked event chain'''

copylink = acopylink


class mcopylink(ManQMixin, CopyMixin):

    '''manually balanced copy linked event chain'''


class scopylink(SyncQMixin, CopyMixin):

    '''autosynchronized copy linked event chain'''

###############################################################################
## active repeat linked event chain ###########################################
###############################################################################


class arepeatlink(AutoQMixin, RepeatMixin):

    '''auto-balanced repeat linked event chain'''

repeatq = arepeatlink


class mrepeatlink(ManQMixin, RepeatMixin):

    '''manually balanced repeat linked event chain'''


class srepeatlink(SyncQMixin, RepeatMixin):

    '''autosynchronized repeat linked event chain'''

###############################################################################
## active mapping linked event chain ##########################################
###############################################################################


class amaplink(AutoQMixin, MapMixin):

    '''auto-balanced map linked event chain'''

maplink = amaplink


class mmaplink(ManQMixin, MapMixin):

    '''manually balanced map linked event chain'''


class smaplink(SyncQMixin, MapMixin):

    '''autosynchronized map linked event chain'''

__all__ = sorted(name for name, obj in port.items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
