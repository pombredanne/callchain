# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''twoq queuing mixins'''

from appspace.keys import AppspaceKey


class Queueing(AppspaceKey):

    '''queuing key'''

    def args(*args, **kw):
        '''arguments for current callable'''

    def tap(call):
        '''
        add call

        @param call: a call
        '''

    def detap():
        '''clear call'''

    def wrap(call):
        '''build factory callable and make call'''

    def unwrap():
        '''clear call'''
        
    def ahead(n=None):
        '''
        move iterator n-steps ahead or, if n is `None`, consume entirely

        @param n: number of steps to advance (default: None)
        '''

    def outcount():
        '''count of outgoing items'''

    @property
    def balanced():
        '''if queues are balanced'''

    def index(thing):
        '''
        insert thing into incoming things

        @param thing: some thing
        '''

    def end():
        '''return outgoing things and clear'''

    def results():
        '''iterate over reversed outgoing things, clearing as it goes'''

    def value():
        '''return outgoing things and clear outgoing things'''

    def first():
        '''first thing among incoming things'''

    def last():
        '''last thing among incoming things'''

    ###########################################################################
    ## clear queues ###########################################################
    ###########################################################################

    def remove(thing):
        '''
        remove thing from incoming things

        @param thing: some thing
        '''

    def clear():
        '''clear all queues'''

    def inclear():
        '''incoming things clear'''

    def outclear():
        '''incoming things clear'''

    ###########################################################################
    ## manipulate queues ######################################################
    ###########################################################################

    def append(thing):
        '''incoming things right append'''

    def appendleft(thing):
        '''incoming things left append'''

    def insert(index, value):
        '''
        insert thing into incoming things

        @param index: index position
        @param thing: some thing
        '''

    def extend(things):
        '''incoming things right extend'''

    def extendleft(things):
        '''incoming things left extend'''

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
