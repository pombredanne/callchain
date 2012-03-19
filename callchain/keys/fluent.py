# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''fluent keys'''

from appspace.keys import AppspaceKey


class KChain(AppspaceKey):

    '''callchain key'''

    def callchain(call, key=False, *args, **kw):
        '''
        add `call` or appspaced `call` to call callchain, partializing it with any
        passed arguments

        @param call: call or appspaced call label
        @param key: appspace key (default: False)
        '''


class KEvent(KChain):

    '''eventchain key'''

    def on(eventchain, call, key=False, *args, **kw):
        '''
        bind call to `eventchain`

        @param eventchain: eventchain label
        @param call: label for call or eventspaced thing
        @param key: key label (default: False)
        '''

    def off(eventchain):
        '''
        clear calls bound to `eventchain`

        @param eventchain: eventchain label
        '''

    def trigger(*events):
        '''
        extend primary call callchain with partials bound to `events`
        
        @param *events: eventchain labels
        '''
