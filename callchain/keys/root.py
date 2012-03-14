# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''root keys'''

from appspace.keys import AppspaceKey


class KBackRoot(AppspaceKey):
    
    '''root back key'''

    def back(link):
        '''
        handle chainlet end

        @param link: linked chain
        '''


class KChainRoot(KBackRoot):

    '''root chain key'''

    def __call__(*args):
        '''new chain session'''


class KEventRoot(KChainRoot):

    '''root event key'''

    def event(event):
        '''
        create or fetch ``event``

        @param event: event label
        '''

    def unevent(event):
        '''
        drop ``event``

        @param event: event label
        '''
