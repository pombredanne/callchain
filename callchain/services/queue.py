# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''twoq queuing mixins'''

from appspace.keys import AppspaceKey, Attribute


class KService(AppspaceKey):

    '''service key'''


class KQueue(KService):

    '''queuing key'''
    
    incoming = Attribute('incoming queue')
    outgoing = Attribute('outgoing queue')
    balanced = Attribute('if queues are balanced')

    def outcount():
        '''count of outgoing things'''

    def clear():
        '''clear every thing'''

    def inclear():
        '''clear incoming things'''

    def outclear():
        '''clear outgoing things'''
        
    def __iter__():
        '''yield outgoing things, clearing outgoing things as it iterates'''

    def _wclear():
        '''clear work queue'''

    def _uclear():
        '''clear utility queue'''

    def ro():
        '''switch to read-only mode'''

    def ctx1(workq='incoming'):
        '''switch to ctx1-armed context manager'''

    def ctx2(workq='_work', outq='incoming'):
        '''switch to two-armed context manager'''

    def ctx3(workq='_work', outq='outgoing', inq='incoming'):
        '''switch to three-armed context manager'''

    def ctx4(**kw):
        '''switch to four-armed context manager'''

    def autoctx(**kw):
        '''switch to auto-synchronizing context manager'''

    def swap(**kw):
        '''swap queues'''

    def unswap():
        '''rotate queues to default'''
        
    def rw():
        '''rotate queues to default'''


class KCallable(KService):
    
    '''current callable management key'''
    
    def args(*args, **kw):
        '''arguments for current callable'''

    def tap(call, label=True):
        '''
        add call

        @param call: a call
        '''

    def detap():
        '''clear call'''

    def wrap(call):
        '''build factory callable and make call'''

    def unwrap():
        '''clear factory'''
        

class KFinger(KService):  

    '''manipulate queues'''
    
    def ahead(n=None):
        '''
        move iterator n-steps ahead or, if n is `None`, consume entirely

        @param n: number of steps to advance (default: None)
        '''

    def append(thing):
        '''
        append `thing` to right side of incoming things 
        
        @param thing: some thing
        '''

    def appendleft(thing):
        '''
        append `thing` to left side of incoming things 
        
        @param thing: some thing
        '''

    def extend(things):
        '''
        extend right side of incoming things with `things`
        
        @param thing: some things
        '''

    def extendleft(things):
        '''
        extend left side of incoming things with `things`
        
        @param thing: some things
        '''

    def outextend(things):
        '''
        extend right side of outgoing things with `things`

        @param thing: some things
        '''
        
    def reup():
        '''put incoming things in incoming things as one incoming thing'''

    def shift():
        '''shift outgoing things to incoming things'''

    def sync():
        '''
        shift outgoing things to incoming things, clearing incoming things
        '''

    def outshift():
        '''shift incoming things to outgoing things'''

    def outsync():
        '''
        shift incoming things to outgoing things, clearing outgoing things
        '''


class KResults(KService):

    def end():
        '''return outgoing things and clear out all things'''

    def results():
        '''yield outgoing things and clear outgoing things'''

    def value():
        '''return outgoing things and clear outgoing things'''

    def first():
        '''first incoming thing'''

    def last():
        '''last incoming thing'''
