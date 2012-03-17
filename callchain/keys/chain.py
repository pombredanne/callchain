# -*- coding: utf-8 -*-
'''chain keys'''

from callchain.keys.queued import KQueuedRoot
from callchain.keys.fluent import KChain, KEvent
from callchain.keys.call import KChainCall, KEventCall
from callchain.keys.root import KChainRoot, KEventRoot
from callchain.keys.manager import KManager, KEventManager


class KCallChain(KChainCall, KManager, KChainRoot, KChain):

    '''call chain key'''


class KCallChainQ(KCallChain, KQueuedRoot):

    '''queued call chain key'''


class KEventChain(KEventCall, KEventManager, KEventRoot, KEvent):

    '''event chain key'''


class KEventChainQ(KEventChain, KQueuedRoot):

    '''queued event chain key'''
