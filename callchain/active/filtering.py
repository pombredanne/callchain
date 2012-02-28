# -*- coding: utf-8 -*-
'''twoq active filtering linked call chains'''

from inspect import ismodule

from twoq.support import port
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from twoq.active.mixins import AutoQMixin, ManQMixin, SyncQMixin

###############################################################################
## active collecting linked call chains #######################################
###############################################################################


class acollectchain(AutoQMixin, CollectMixin):

    '''auto-balanced collecting linked call chain'''

collectchain = acollectchain


class mcollectchain(ManQMixin, CollectMixin):

    '''manually balanced collecting linked call chain'''


class scollectchain(SyncQMixin, CollectMixin):

    '''autosynchronized collecting linked call chain'''

###############################################################################
## active set linked call chains ##############################################
###############################################################################


class asetchain(AutoQMixin, SetMixin):

    '''auto-balanced set linked call chain'''

setchain = asetchain


class msetchain(ManQMixin, SetMixin):

    '''manually balanced set linked call chain'''


class ssetchain(SyncQMixin, SetMixin):

    '''autosynchronized set linked call chain'''

###############################################################################
## active slice linked call chains ############################################
###############################################################################


class aslicechain(AutoQMixin, SliceMixin):

    '''auto-balanced slice linked call chain'''

slicechain = aslicechain


class mslicechain(ManQMixin, SliceMixin):

    '''manually balanced slice linked call chain'''


class sslicechain(SyncQMixin, SliceMixin):

    '''autosynchronized slice linked call chain'''

###############################################################################
## active filter linked call chains ###########################################
###############################################################################


class afilterchain(AutoQMixin, FilterMixin):

    '''auto-balanced filtering linked call chain'''

filterchain = afilterchain


class mfilterchain(ManQMixin, FilterMixin):

    '''manually balanced filtering linked call chain'''


class sfilterchain(SyncQMixin, FilterMixin):

    '''autosynchronized filtering linked call chain'''

__all__ = sorted(name for name, obj in port.items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
