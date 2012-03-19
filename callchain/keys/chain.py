# -*- coding: utf-8 -*-
'''chain keys'''

from callchain.keys.queued import KQueuedRoot
from callchain.keys.fluent import KChain, KEvent
from callchain.keys.call import KCall, KEventCall
from callchain.keys.root import KChainRoot, KEventRoot, KManager, KEventManager


class KChain(KCall, KManager, KChainRoot, KChain):

    '''call chain key'''


class KChainQ(KChain, KQueuedRoot):

    '''queued call chain key'''


class KEventChain(KEventCall, KEventManager, KEventRoot, KEvent):

    '''event chain key'''


class KEventChainQ(KEventChain, KQueuedRoot):

    '''queued event chain key'''
