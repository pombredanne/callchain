# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''event chain keys'''

from inspect import ismodule

from stuf.six import items
from callchain.mixins.chains.keys import ACallChain


class AEvents(ACallChain):
    
    '''events key'''
    
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

    def commit(self):
        '''run call chain'''

    def events(*events):
        '''
        ordered mapping of per event processing queue

        @param *events: event labels
        '''
        
    def fire(*events):
        '''invoke callables bound to `*events` immediately'''

    def trigger(*events):
        '''add callables bound to events to primary call chain'''


class AEventChain(AEvents):

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


class AEventLink(AEvents):

    '''linked event chain key'''


__all__ = sorted(name for name, obj in items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
