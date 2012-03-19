# -*- coding: utf-8 -*-
'''event chain keys'''

from callchain.keys.core import KEvent
from callchain.keys.queued import KQueued
from callchain.keys.call import KEventCall
from callchain.keys.queued import KQueuedRoot
from callchain.keys.root import KEventRoot, KEventManager
from callchain.keys.branch import KEventBranch, KBranchlet


class KEventChain(KEventCall, KEventManager, KEventRoot, KEvent):

    '''event chain key'''


class KEventChainQ(KEventChain, KQueuedRoot):

    '''queued event chain key'''


class KEventLink(KEventBranch, KEvent, KEventCall):

    '''event link chain key'''


class KEventLinkQ(KEventLink, KQueued):

    '''queued event link chain key'''


class KEventlet(KEventBranch, KBranchlet, KEvent):

    '''eventlet key'''


class KEventletQ(KEventlet, KQueued):

    '''queued eventlet key'''
