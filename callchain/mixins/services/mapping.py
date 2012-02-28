# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''mapping services keys'''

from appspace.keys import AppspaceKey


class SDelay(AppspaceKey):

    '''delayed map key'''

    def delay_each(wait):
        '''
        invoke call with passed arguments, keywords in incoming things after a
        delay

        @param wait: time in seconds
        '''

    def delay_invoke(name, wait):
        '''
        invoke call on each incoming thing with passed arguments, keywords
        after a delay but return incoming thing instead if call returns None

        @param name: name of method
        @param wait: time in seconds
        '''

    def delay_map(wait):
        '''
        invoke call on each incoming thing after a delay

        @param wait: time in seconds
        '''


class SCopy(AppspaceKey):

    '''duplication key'''

    def copy(self):
        '''copy each incoming thing'''

    def deepcopy(self):
        '''copy each incoming thing deeply'''


class SMapping(AppspaceKey):

    '''map key'''

    def each():
        '''invoke call with passed arguments, keywords in incoming things'''

    def invoke(name):
        '''
        invoke call on each incoming thing with passed arguments, keywords
        but return incoming thing instead if call returns None

        @param name: name of method
        '''

    def items():
        '''invoke call on each mapping to get key, value pairs'''

    def map():
        '''invoke call on each incoming thing'''

    def starmap():
        '''invoke call on each incoming pair of things'''


class SRepeat(AppspaceKey):

    '''repetition key'''

    def padnone():
        '''
        incoming things and then `None` indefinitely

        (Useful for emulating the behavior of 2.x classic `builtin` `map`)
        '''

    def range(start, stop=0, step=1):
        '''
        repeat incoming things `n` times

        @param n: number of times to repeat
        '''

    def repeat(n):
        '''
        repeat incoming things `n` times

        @param n: number of times to repeat
        '''

    def times(n=None):
        '''
        repeat call with passed arguments

        @param n: number of times to repeat calls (default: None)
        '''


class SMap(SDelay, SCopy, SMapping, SRepeat):

    '''mapping key'''
