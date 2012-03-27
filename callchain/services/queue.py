# -*- coding: utf-8 -*-
'''twoq queuing mixins'''

from appspace.keys import AppspaceKey, Attribute


class KService(AppspaceKey):

    '''service key'''


class KThings(KService):

    '''queuing key'''

    incoming = Attribute('incoming queue')
    outgoing = Attribute('outgoing queue')
    balanced = Attribute('if incoming and outgoing things are balanced')

    def __len__():  # @NoSelf
        '''number of incoming things'''

    def outcount():  # @NoSelf
        '''number of outgoing things'''

    ###########################################################################
    ## queue clearance ########################################################
    ###########################################################################

    def clear():  # @NoSelf
        '''clear every thing'''

    def inclear():  # @NoSelf
        '''clear incoming things'''

    def outclear():  # @NoSelf
        '''clear outgoing things'''

    ###########################################################################
    ## context rotation #######################################################
    ###########################################################################

    def ctx1(**kw):  # @NoSelf
        '''swap to one-armed context'''

    def ctx2(**kw):  # @NoSelf
        '''swap to two-armed context'''

    def ctx3(**kw):  # @NoSelf
        '''swap to three-armed context'''

    def ctx4(**kw):  # @NoSelf
        '''swap to four-armed context'''

    def autoctx(**kw):  # @NoSelf
        '''swap to auto-synchronizing context'''

    def ro():  # @NoSelf
        '''swap to read-only context'''

    def swap(**kw):  # @NoSelf
        '''swap contexts'''

    def reswap(self):  # @NoSelfs
        '''swap to current preferred context'''

    def unswap():  # @NoSelf
        '''swap to default context'''

    def rw():  # @NoSelf
        '''swap to default context'''

    ###########################################################################
    ## current callable management ############################################
    ###########################################################################

    def args(*args, **kw):  # @NoSelf
        '''arguments for current callable'''

    def detap():  # @NoSelf
        '''clear current callable'''

    def wrap(call):  # @NoSelf
        '''
        build current callable from factory

        @param call: a callable
        '''

    def unwrap():  # @NoSelf
        '''clear factory'''

    ###########################################################################
    ## things rotation ########################################################
    ###########################################################################

    def outshift():  # @NoSelf
        '''shift incoming things to outgoing things'''

    def outsync():  # @NoSelf
        '''
        shift incoming things to outgoing things, clearing outgoing things
        '''

    def reup():  # @NoSelf
        '''put incoming things in incoming things as one incoming thing'''

    def shift():  # @NoSelf
        '''shift outgoing things to incoming things'''

    def sync():  # @NoSelf
        '''
        shift outgoing things to incoming things, clearing incoming things
        '''

    ###########################################################################
    ## things appending #######################################################
    ###########################################################################

    def append(thing):  # @NoSelf
        '''
        append `thing` to right side of incoming things

        @param thing: some thing
        '''

    def appendleft(thing):  # @NoSelf
        '''
        append `thing` to left side of incoming things

        @param thing: some thing
        '''

    ###########################################################################
    ## things extension #######################################################
    ###########################################################################

    def extend(things):  # @NoSelf
        '''
        extend right side of incoming things with `things`

        @param thing: some things
        '''

    def extendleft(things):  # @NoSelf
        '''
        extend left side of incoming things with `things`

        @param thing: some things
        '''

    def outextend(things):  # @NoSelf
        '''
        extend right side of outgoing things with `things`

        @param thing: some things
        '''

    ###########################################################################
    ## iteration runners ######################################################
    ###########################################################################

    def __iter__():  # @NoSelf
        '''yield outgoing things, clearing outgoing things as it iterates'''

    def breakcount(call, length, exception=StopIteration):  # @NoSelf
        '''
        rotate through iterator until it reaches its original length

        @param iterable: an iterable to exhaust
        '''

    def exhaust(iterable, exception=StopIteration):  # @NoSelf
        '''
        call next on an iterator until it's exhausted

        @param iterable: iterable to exhaust
        @param exception: exception marking end of iteration
        '''

    def exhaustmap(map, call, filter=False, exception=StopIteration):  # @NoSelf @IgnorePep8
        '''
        call `next` on an iterator until it's exhausted

        @param mapping: a mapping to exhaust
        @param call: call to handle what survives the filter
        @param filter: a filter to apply to mapping (default: `None`)
        @param exception: exception sentinel (default: `StopIteration`)
        '''

    def iterexcept(call, exception, start=None):  # @NoSelf
        '''
        call a function repeatedly until an exception is raised

        Converts a call-until-exception interface to an iterator interface.
        Like `iter(call, sentinel)` but uses an exception instead of a sentinel
        to end the loop.

        Raymond Hettinger, Python Cookbook recipe # 577155
        '''


class KResult(KThings):

    def end():  # @NoSelf
        '''return outgoing things then clear out everything'''

    def first():  # @NoSelf
        '''first incoming thing'''

    def last():  # @NoSelf
        '''last incoming thing'''

    def peek():  # @NoSelf
        '''results from read-only context'''

    def results():  # @NoSelf
        '''yield outgoing things, clearing outgoing things as it iterates'''

    def value():  # @NoSelf
        '''return outgoing things and clear outgoing things'''
