# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''fluent keys'''

from appspace.keys import AppspaceKey


class KChain(AppspaceKey):

    '''chain key'''

    def chain(call, key=False, *args, **kw):
        '''
        add `call` or appspaced `call` to call chain, partializing it with any
        passed arguments

        @param call: call or appspaced call label
        @param key: appspace key (default: False)
        '''


class KEvent(KChain):

    '''event key'''

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
        extend primary call chain with partials bound to `events`
        
        @param *events: event labels
        '''
