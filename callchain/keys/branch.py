# -*- coding: utf-8 -*-
'''branch keys'''

from appspace.keys import Attribute

from callchain.keys.reset import KCore


class KBranch(KCore):

    ''''branch key'''

    G = Attribute('root external global settings')
    M = Attribute('root external appspace manager')
    _G = Attribute('root internal global settings')
    _M = Attribute('root internal appspace manager')
    root = Attribute('root object')


class KEventBranch(KBranch):

    '''event branch key'''

    E = Attribute('local event registry')


class KLinked(KBranch):

    '''linked chain mixin'''

    def close():  # @NoSelf
        '''close out linked chain and switch to root chain'''


class KChainletKey(KBranch):

    def back():  # @NoSelf
        '''switch back to root chain'''
