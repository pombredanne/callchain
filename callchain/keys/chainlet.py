# -*- coding: utf-8 -*-
'''chainlet keys'''

from callchain.keys.queued import KQueued
from callchain.keys.fluent import KChain, KEvent
from callchain.keys.rooted import KRooted, KRootlet, KEventRooted


class KCallChainlet(KRooted, KRootlet, KChain):

    '''call chainlet key'''


class KCallChainletQ(KCallChainlet, KQueued):

    '''queued call chainlet key'''


class KEventlet(KEventRooted, KRootlet, KEvent):

    '''eventlet key'''


class KEventletQ(KEventlet, KQueued):

    '''queued eventlet key'''
