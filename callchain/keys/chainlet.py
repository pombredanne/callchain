# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''chainlet keys'''

from appspace.keys import AppspaceKey

from callchain.keys.queued import KQueued
from callchain.keys.fluent import KChain, KEvent
from callchain.keys.branch import KBranch, KEventBranch


class KBranchlet(AppspaceKey):
    
    '''rootlet key'''

    def back():
        '''revert to root chain'''


class KChainlet(KBranch, KBranchlet, KChain):

    '''call chainlet key'''


class KChainletQ(KChainlet, KQueued):

    '''queued call chainlet key'''


class KEventlet(KEventBranch, KBranchlet, KEvent):

    '''eventlet key'''


class KEventletQ(KEventlet, KQueued):

    '''queued eventlet key'''
