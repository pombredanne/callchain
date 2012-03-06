# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''call chain keys'''

from appspace.keys import AppspaceKey
from octopus.keys import AOctopus, ATentacle

__all__ = ('KChain', 'KCallChain', 'KChainLink')


class KChain(AppspaceKey):
    
    '''chains key'''

    def commit():
        '''run call chain'''

    def chain(call, key=False, *args, **kw):
        '''
        add callable or appspaced application to call chain, partializing it
        with any passed parameters

        @param call: callable or application label
        @param key: key label (default: False)
        '''
        
    def unchain(key):
        '''
        unchain callables or appspaced applications from a call chain

        @param call: callable or application label
        @param key: key label (default: False)
        '''


class KCallChain(AOctopus, KChain):

    '''call chain key'''
    
    def switch(label, key=False):
        '''
        switch to linked call chain

        @param label: linked call chain label
        @param key: linked call chain key (default: False)
        '''
    
    def back(link):
        '''return to root call chain'''


class KChainLink(ATentacle, KChain):

    '''linked call chain key'''
    
    def back():
        '''return to root call chain'''