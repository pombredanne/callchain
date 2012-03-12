# -*- coding: utf-8 -*-
'''linked chain keys'''

from callchain.keys.queued import KQueued
from callchain.keys.fluent import KChain, KEvent
from callchain.keys.call import KChainCall, KEventCall
from callchain.keys.rooted import KChainRooted, KEventRooted


class KLinkedChain(KChainRooted, KChain, KChainCall):

    '''linked call chain key'''


class KLinkedQ(KLinkedChain, KQueued):

    '''queued linked call chain key'''


class KEventlink(KEventRooted, KEvent, KEventCall):

    '''event link chain key'''


class KEventlinkQ(KEventlink, KQueued):

    '''queued event link chain key'''
