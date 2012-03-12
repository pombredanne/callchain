# -*- coding: utf-8 -*-
'''chain keys'''

from callchain.keys.queued import KQueued
from callchain.keys.fluent import KChain, KEvent
from callchain.keys.call import KChainCall, KEventCall
from callchain.keys.root import KChainRoot, KEventRoot
from callchain.keys.manager import KChainManager, KEventManager


class KCallChain(KChainCall, KChainManager, KChainRoot, KChain):

    '''call chain key'''


class KCallChainQ(KCallChain, KQueued):

    '''queued call chain key'''


class KEventChain(KEventCall, KEventManager, KEventRoot, KEvent):

    '''event chain key'''


class KEventChainQ(KEventChain, KQueued):

    '''queued event chain key'''
