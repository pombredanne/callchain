# -*- coding: utf-8 -*-
'''linked chain keys'''

from callchain.keys.queued import KQueued
from callchain.keys.fluent import KChain, KEvent
from callchain.keys.call import KChainCall, KEventCall
from callchain.keys.rooted import KRooted, KEventRooted


class KLinkedChain(KRooted, KChain, KChainCall):

    '''linked call chain key'''


class KLinkedQ(KLinkedChain, KQueued):

    '''queued linked call chain key'''


class KEventLink(KEventRooted, KEvent, KEventCall):

    '''event link chain key'''


class KEventlinkQ(KEventLink, KQueued):

    '''queued event link chain key'''
