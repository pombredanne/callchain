# -*- coding: utf-8 -*-
'''chainlink chains'''

from appspace.keys import appifies

from callchain.keys.linked import (
    KLinked, KLinkedQ, KEventLink, KEventlinkQ)

from callchain.root import LiteMixin
from callchain.queued import QBranchMixin
from callchain.fluent import ChainMixin, EventMixin
from callchain.call import CallMixin, EventCallMixin
from callchain.branch import BranchMixin, EventBranchMixin, LitedMixin

###############################################################################
## linked chain ###############################################################
###############################################################################


@appifies(KLinked)
class Linked(BranchMixin, ChainMixin, CallMixin):

    '''linked call chain'''


@appifies(KLinked)
class chainlink(LiteMixin, LitedMixin, Linked):

    '''lite linked call chain'''


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
class eventlink(LitedMixin, EventLink):

    '''lite linked event chain'''


@appifies(KEventlinkQ)
class EventLinkQ(QBranchMixin, EventLink):

    '''queued linked event chain'''
