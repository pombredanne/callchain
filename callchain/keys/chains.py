# -*- coding: utf-8 -*-
'''chain keys'''

from callchain.keys.call import KCall
from callchain.keys.core import KChain
from callchain.keys.root import KChainRoot, KManager
from callchain.keys.branch import KBranch, KBranchlet
from callchain.keys.queued import KQueued, KQueuedRoot


class KChain(KCall, KManager, KChainRoot, KChain):

    '''chain key'''


class KChainQ(KChain, KQueuedRoot):

    '''queued chain key'''


class KLinked(KBranch, KChain, KCall):

    '''linked chain key'''


class KLinkedQ(KLinked, KQueued):

    '''queued linked chain key'''


class KChainlet(KBranch, KBranchlet, KChain):

    '''chainlet key'''


class KChainletQ(KChainlet, KQueued):

    '''queued chainlet key'''
