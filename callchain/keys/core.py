# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''callchain core keys'''

from appspace.keys import AppspaceKey


class KSettings(AppspaceKey):

    '''settings key'''


class KDefaults(AppspaceKey):

    '''default settings key'''


class KRequired(AppspaceKey):

    '''required settings key'''
    
    
class KChain(AppspaceKey):

    '''chain key'''

    def callchain(call, key=False, *args, **kw):
        '''
        add `call` or appspaced `call` to call callchain, partializing it with any
        passed arguments

        @param call: call or appspaced call label
        @param key: appspace key (default: False)
        '''


class KEvent(KChain):

    '''event chain key'''

    def on(event, call, key=False, *args, **kw):
        '''
        bind call to `event`

        @param event: event label
        @param call: label for call or eventspaced thing
        @param key: key label (default: False)
        '''

    def off(event):
        '''
        clear calls bound to `event`

        @param event: event label
        '''

    def trigger(*events):
        '''
        extend primary call callchain with partials bound to `events`
        
        @param *events: event labels
        '''



class NoServiceError(Exception):

    '''no service error'''
