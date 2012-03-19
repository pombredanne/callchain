# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''root keys'''

from appspace.keys import AppspaceKey


class KChainRoot(AppspaceKey):

    '''root chain key'''

    def __call__(*args):
        '''new chain session'''

    def back(chainlink):
        '''
        handle chainlet end

        @param chainlink: chainlink chain
        '''


class KEventRoot(KChainRoot):

    '''root eventchain key'''

    def eventchain(eventchain):
        '''
        create or fetch `eventchain`

        @param eventchain: eventchain label
        '''

    def unevent(eventchain):
        '''
        drop `eventchain`

        @param eventchain: eventchain label
        '''
