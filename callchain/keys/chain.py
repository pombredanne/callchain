# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''callchain core keys'''

from appspace.keys import AppspaceKey

from callchain.keys.octopus import AOctopus, ATentacle

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
        
        
class KChainlet(ATentacle, KChain):

    '''linked call chain key'''
    
    def back():
        '''return to root call chain'''
        
        
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
