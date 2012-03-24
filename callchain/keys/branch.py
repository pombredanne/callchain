# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
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

    def __init__(root):
        '''
        init

        @param root: root object
        '''


class KEventBranch(KBranch):

    '''event branch key'''
    
    E = Attribute('local event registry')


class KBranchlet(KResetLocal):
    
    '''branchlet key'''

    def back():
        '''revert to root chain'''