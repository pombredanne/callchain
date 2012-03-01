# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''call chain keys'''

from callchain.chains.services import KQueue

__all__ = ('KCallChain', 'KChainLink')


class KChain(KQueue):
    
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
        
    def add(app, label, key=False):
        '''
        add application to appspace

        @param app: new application
        @param label: application label
        @param key: key label (default: False)
        '''
    
    def app(label, key=False):
        '''
        make application from appspace current call in chall chain

        @param label: application label
        @param key: key label (default: False)
        '''


class KCallChain(KChain):

    '''call chain key'''
    
    def switch(label, key=False):
        '''
        switch to linked call chain

        @param label: linked call chain label
        @param key: linked call chain key (default: False)
        '''


class KChainLink(KChain):

    '''linked call chain key'''
    
    def back():
        '''return to root call chain'''
