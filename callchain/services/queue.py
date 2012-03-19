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
        
    def ahead(n=None):
        '''
        move iterator n-steps ahead or, if n is `None`, consume entirely

        @param n: number of steps to advance (default: None)
        '''

    def outcount():
        '''count of outgoing items'''

    def index(thing):
        '''
        insert thing into incoming things

        @param thing: some thing
        '''

    ###########################################################################
    ## clear queues ###########################################################
    ###########################################################################

    def remove(thing):
        '''
        remove thing from incoming things

        @param thing: some thing
        '''

    def clear():
        '''clear every thing'''

    def inclear():
        '''clear incoming things'''

    def outclear():
        '''clear outgoing things'''

    ###########################################################################
    ## manipulate queues ######################################################
    ###########################################################################

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

    def insert(index, thing):
        '''
        insert thing into incoming things

        @param index: index position
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

    ###########################################################################
    ## balance queues #########################################################
    ###########################################################################

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


class KResults(KQueue):

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
