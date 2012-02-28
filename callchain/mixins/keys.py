# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''callchain keys'''

from appspace.keys import Attribute

from callchain.mixins.services.queuing import Queueing

__all__ = ('ACallChain', 'AChainLink')


class AChains(Queueing):
    
    '''chains key'''
    
    G = Attribute('application settings')
    L = Attribute('local manager settings')
    port = Attribute('python 2.x <-> python 3.x compatibility helper')
    space = Attribute('appspace')
    
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
        
    def commit(self):
        '''invoke call chain'''

    def chain(call, key=False, *args, **kw):
        '''
        add callable or appspaced application to call chain, partializing it
        with any passed parameters

        @param call: callable or application label
        @param key: key label (default: False)
        '''


class ACallChain(AChains):

    '''call chain key'''
    
    def link(label, branch):
        '''
        add linked call chain class

        @param label: linked call chain class label
        @param branch: linked call chain class
        '''

    def switch(label):
        '''
        switch to linked call chain

        @param label: chain label
        '''


class AChainLink(AChains):

    '''linked call chain key'''
    
    def back():
        '''return to root call chain'''
