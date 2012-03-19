# -*- coding: utf-8 -*-
'''chainlink chains'''

from appspace.keys import appifies

from callchain.root import SingleMixin
from callchain.queued import QBranchMixin
from callchain.keys.linked import (
    KLinked, KLinkedQ, KEventLink, KEventlinkQ)
from callchain.fluent import ChainMixin, EventMixin
from callchain.call import CallMixin, EventCallMixin
from callchain.rooted import BranchMixin, EventBranchMixin, RootedMixin

###############################################################################
## linked chain ###############################################################
###############################################################################


@appifies(KLinked)
class Linked(BranchMixin, ChainMixin, CallMixin):

    '''linked call chain'''


@appifies(KLinked)
class chainlink(SingleMixin, RootedMixin, Linked):

    '''root linked call chain'''


@appifies(KLinkedQ)
class LinkedQ(QBranchMixin, Linked):

    '''queued linked call chain'''


###############################################################################
## linked event ###############################################################
###############################################################################


@appifies(KEventLink)
class EventLink(EventBranchMixin, EventMixin, EventCallMixin):

    '''linked event chain'''


@appifies(KEventLink)
class eventlink(RootedMixin, EventLink):

    '''root linked event chain'''


@appifies(KEventlinkQ)
class EventLinkQ(QBranchMixin, EventLink):

    '''queued linked event chain'''
