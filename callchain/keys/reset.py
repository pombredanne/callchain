# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''reset keys'''

from appspace.keys import AppspaceKey


class KResetType(AppspaceKey):

    '''reset type key'''

    def reset():
        '''reset previously accessed ``lazybase`` attributes'''


class KResetLocal(KResetType):

    '''reset thread local key'''