# -*- coding: utf-8 -*-
'''callchain reset keys'''

from appspace.keys import AppspaceKey, Attribute


class KResetType(AppspaceKey):

    '''reset type key'''

    def reset():  # @NoSelf
        '''reset previously accessed `lazybase` attributes'''


class KResetLocal(KResetType):

    '''reset thread local key'''


class KCore(KResetLocal):

    '''core key'''

    G = Attribute('external application global settings')

    def __init__(root):  # @NoSelf
        '''
        init

        @param root: root chain
        '''


class KConfig(KCore):

    '''configuration access key'''

    defaults = Attribute('default settings by their lonesome')
    required = Attribute('required settings by their lonesome')
