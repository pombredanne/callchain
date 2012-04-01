# -*- coding: utf-8 -*-
'''callchain generic mixins'''

from callchain.core import CoreMixin
from callchain.chain import (
    RootMixin, EventRootMixin, BranchMixin, ChainletMixin, EventBranchMixin,
    LinkedMixin)
from callchain.call import ChainMixin, PriorityMixin, EventMixin

###############################################################################
## chainlet ###################################################################
###############################################################################


class chainlet(ChainletMixin, BranchMixin, CoreMixin):

    '''generic chainlet mixin'''


class eventlet(ChainletMixin, EventBranchMixin, CoreMixin):

    '''generic eventlet mixin'''


###############################################################################
## linked chain ###############################################################
###############################################################################


class chainlink(BranchMixin, LinkedMixin, ChainMixin):

    '''generic linked chain'''


class prioritylink(BranchMixin, LinkedMixin, PriorityMixin):

    '''generic priority linked chain'''


class eventlink(EventBranchMixin, LinkedMixin, EventMixin):

    '''generic linked event chain'''


###############################################################################
## chain ######################################################################
###############################################################################


class callchain(RootMixin, ChainMixin):

    '''generic call chain'''


class prioritychain(RootMixin, PriorityMixin):

    '''generic priority chain generic'''


class eventchain(EventRootMixin, EventMixin):

    '''generic event chain'''
