# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''call keys'''

from appspace.keys import AppspaceKey, Attribute


class KCall(AppspaceKey):

    '''call key'''

    L = Attribute('local settings')
    Meta = Attribute('local settings')
    port = Attribute('python 2.x <-> python 3.x compatibility helper')
    space = Attribute('external appspace interface')

    def switch(label, key=False):
        '''
        overt switch to linked call chain from external appspace

        @param label: linked call chain label
        @param key: linked call chain chain key (default: False)
        '''
        
class KChainCall(KCall):
    
    '''chain call key'''
    
    def commit():
        '''consume call chain until exhausted'''
        
  
class KEventCall(KChainCall):
    
    '''event call key'''
      
    def fire(*events):
        '''
        run calls bound to ``events`` NOW

        @param *events: event labels
        '''

    def queues(*events):
        '''
        ordered mapping of processing queues for ``events``

        @param *events: event labels
        '''