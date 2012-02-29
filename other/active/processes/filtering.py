# -*- coding: utf-8 -*-
'''active filtering linked event chains'''

from inspect import ismodule

from twoq.support import port
from twoq.mixins.filtering import (
    FilterMixin, CollectMixin, SetMixin, SliceMixin)

from twoq.active.mixins import AutoQMixin, ManQMixin, SyncQMixin

###############################################################################
## active collecting linked event chain #######################################
###############################################################################


class acollectlink(AutoQMixin, CollectMixin):

    '''auto-balanced collecting linked event chain'''

collectevent = acollectlink


class mcollectlink(ManQMixin, CollectMixin):

    '''manually balanced collecting linked event chain'''


class scollectlink(SyncQMixin, CollectMixin):

    '''autosynchronized collecting linked event chain'''

###############################################################################
## active set linked event chain ##############################################
###############################################################################


class asetlink(AutoQMixin, SetMixin):

    '''auto-balanced set linked event chain'''

setlink = asetlink


class msetlink(ManQMixin, SetMixin):

    '''manually balanced set linked event chain'''


class ssetlink(SyncQMixin, SetMixin):

    '''autosynchronized set linked event chain'''

###############################################################################
## active slice linked event chain ############################################
###############################################################################


class aslicelink(AutoQMixin, SliceMixin):

    '''auto-balanced slice linked event chain'''

slicelink = aslicelink


class mslicelink(ManQMixin, SliceMixin):

    '''manually balanced slice linked event chain'''


class sslicelink(SyncQMixin, SliceMixin):

    '''autosynchronized slice linked event chain'''

###############################################################################
## active filter linked event chain ###########################################
###############################################################################


class afilterlink(AutoQMixin, FilterMixin):

    '''auto-balanced filter linked event chain'''

filterlink = afilterlink


class mfilterlink(ManQMixin, FilterMixin):

    '''manually balanced filtering linked event chain'''


class sfilterlink(SyncQMixin, FilterMixin):

    '''autosynchronized filter linked event chain'''

__all__ = sorted(name for name, obj in port.items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
