# -*- coding: utf-8 -*-
'''linked chain keys'''

from callchain.keys.queued import KQueued
from callchain.keys.fluent import KChain, KEvent
from callchain.keys.call import KCall, KEventCall
from callchain.keys.rooted import KBranch, KEventBranch


class KLinked(KBranch, KChain, KCall):

    '''linked call chain key'''


class KLinkedQ(KLinked, KQueued):

    '''queued linked call chain key'''


class KEventLink(KEventBranch, KEvent, KEventCall):

    '''event link chain key'''


class KEventlinkQ(KEventLink, KQueued):

    '''queued event link chain key'''
