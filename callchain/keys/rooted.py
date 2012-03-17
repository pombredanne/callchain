# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''rooted keys'''

from appspace.keys import AppspaceKey, Attribute


class KRootlet(AppspaceKey):
    
    '''rootlet key'''

    def back():
        '''revert to root chain'''


class KRooted(AppspaceKey):

    ''''rooted chain mixin'''
    
    G = Attribute('root external global settings')
    M = Attribute('root external appspace manager')
    _G = Attribute('root internal global settings')
    _M = Attribute('root internal appspace manager')
    root = Attribute('root object')

    def __init__(root):
        '''
        init

        @param root: root call chain
        '''


class KEventRooted(KRooted):

    '''rooted event chain mixin'''
    
    E = Attribute('local event registry')
