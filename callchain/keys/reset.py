# -*- coding: utf-8 -*-
'''callchain reset keys'''

from appspace.keys import AppspaceKey


class KResetType(AppspaceKey):

    '''reset type key'''

    def reset():  # @NoSelf
        '''reset previously accessed `lazybase` attributes'''


class KResetLocal(KResetType):

    '''reset thread local key'''
