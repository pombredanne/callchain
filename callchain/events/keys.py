# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''event chain keys'''

from callchain.chains.keys import KCallChain, KChain, KChainLink

__all__ = ('KEventChain', 'KEventLink')


class KEvent(KChain):
    
    '''base event key'''
    
    def on(event, call, key=False, *args, **kw):
        '''
        bind callable to event

        @param event: event label
        @param call: callable or application label
        @param key: key label (default: False)
        '''

    def off(event):
        '''
        clear callables bound to event

        @param event: event label
        '''

    def commit():
        '''run call chain'''

    def events(*events):
        '''
        ordered mapping of outgoing items from each event chain

        @param *events: event labels
        '''
        
    def fire(*events):
        '''invoke callables bound to `*events` immediately'''

    def trigger(*events):
        '''add callables bound to events to primary call chain'''


class KEventChain(KCallChain, KEvent):

    '''event chain key'''

    def event(event):
        '''
        create or fetch event

        @param event: event label
        '''

    def unevent(event):
        '''
        drop event

        @param event: event label
        '''


class KEventLink(KChainLink, KEvent):

    '''linked event chain key'''
