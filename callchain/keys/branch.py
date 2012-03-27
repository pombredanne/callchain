# -*- coding: utf-8 -*-
'''branch keys'''

from appspace.keys import Attribute

from callchain.keys.reset import KResetLocal


class KBranch(KResetLocal):

    ''''branch key'''

    G = Attribute('root external global settings')
    M = Attribute('root external appspace manager')
    _G = Attribute('root internal global settings')
    _M = Attribute('root internal appspace manager')
    root = Attribute('root object')

    def __init__(root):  # @NoSelf
        '''
        init

        @param root: root chain
        '''


class KEventBranch(KBranch):

    '''event branch key'''

    E = Attribute('local event registry')


class KLinkedKey(KBranch):

    '''linked chain mixin'''

    def close():  # @NoSelf
        '''close out linked chain and switch to root chain'''


class KChainletKey(KBranch):

    def back():  # @NoSelf
        '''switch back to root chain'''
