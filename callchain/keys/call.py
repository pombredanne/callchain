# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''call keys'''

from appspace.keys import AppspaceKey, Attribute


class KCall(AppspaceKey):

    '''call key'''

    L = Attribute('local settings extracted')
    Meta = Attribute('local settings')
    port = Attribute('python 2.x <-> python 3.x porting helper')
    space = Attribute('external appspace interface')

    def switch(label, key=False):
        '''
        overt switch to linked call chain configured in external appspace

        @param label: linked call chain label
        @param key: linked call chain chain key (default: False)
        '''

    def __enter__():
        '''enter execution context'''

    def __exit__(e, t, b):
        '''exit execution context'''
    
    def commit():
        '''consume call chain until exhausted'''
        
  
class KEventCall(KCall):
    
    '''event call key'''
      
    def fire(*events):
        '''
        run calls bound to `events` **NOW**

        @param *events: event labels
        '''

    def queues(*events):
        '''
        ordered mapping of processing queues for `events`

        @param *events: event labels
        '''
