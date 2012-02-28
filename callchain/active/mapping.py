# -*- coding: utf-8 -*-
'''mapping linked active call chains'''

from inspect import ismodule

from twoq.support import port
from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from twoq.active.mixins import AutoQMixin, ManQMixin, SyncQMixin

###############################################################################
## active delayed mapping linked call chains ##################################
###############################################################################


class adelaylink(AutoQMixin, DelayMixin):

    '''auto-balanced delayed mapping linked call chain'''

delaylink = adelaylink


class mdelaylink(ManQMixin, DelayMixin):

    '''manually balanced delayed mapping linked call chain'''


class sdelaylink(SyncQMixin, DelayMixin):

    '''autosynchronized  delayed mapping linked call chain'''

###############################################################################
## active copy linked call chains #############################################
###############################################################################


class acopylink(AutoQMixin, CopyMixin):

    '''auto-balanced copy linked call chain'''

copylink = acopylink


class mcopylink(ManQMixin, CopyMixin):

    '''manually balanced copy linked call chain'''


class scopylink(SyncQMixin, CopyMixin):

    '''autosynchronized copy linked call chain'''

###############################################################################
## active repeat linked call chains ###########################################
###############################################################################


class arepeatlink(AutoQMixin, RepeatMixin):

    '''auto-balanced repeat linked call chain'''

repeatq = arepeatlink


class mrepeatlink(ManQMixin, RepeatMixin):

    '''manually balanced repeat linked call chain'''


class srepeatlink(SyncQMixin, RepeatMixin):

    '''autosynchronized repeat linked call chain'''

###############################################################################
## active mapping linked call chains ##########################################
###############################################################################


class amaplink(AutoQMixin, MapMixin):

    '''auto-balanced mapping linked call chain'''

maplink = amaplink


class mmaplink(ManQMixin, MapMixin):

    '''manually balanced mapping linked call chain'''


class smaplink(SyncQMixin, MapMixin):

    '''autosynchronized mapping linked call chain'''

__all__ = sorted(name for name, obj in port.items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
