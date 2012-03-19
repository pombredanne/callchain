# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''mapping services keys'''

from callchain.services.queue import KService


class KDelay(KService):

    '''delayed map key'''

    def delay_each(wait):
        '''
        invoke call with passed arguments, keywords in incoming things after
        delay `wait`

        @param wait: time in seconds
        '''

    def delay_invoke(name, wait):
        '''
        invoke method `name` on each incoming thing with passed arguments,
        keywords after delay `wait` but return incoming thing instead if method
        returns `None`

        @param name: name of method
        @param wait: time in seconds
        '''

    def delay_map(wait):
        '''
        invoke call on each incoming thing after delay `wait`

        @param wait: time in seconds
        '''


class KCopy(KService):

    '''copy key'''

    def copy(self):
        '''copy each incoming thing'''

    def deepcopy(self):
        '''copy each incoming thing deeply'''


class KRepeat(KService):

    '''repetition key'''

    def padnone():
        '''incoming things and then `None` indefinitely'''

    def range(start, stop=0, step=1):
        '''
        put sequence of numbers in incoming things

        @param start: number to start with
        @param stop: number to stop with (default: 0)
        @param step: number of steps to advance per iteration (default: 1)
        '''

    def repeat(n):
        '''
        repeat incoming things `n` times

        @param n: number of times to repeat
        '''

    def times(n=None):
        '''
        repeat call with incoming things `n` times

        @param n: number of times to repeat calls with incoming things 
            (default: None)
        '''


class KMap(KService):

    '''mapping key'''

    def each():
        '''invoke call with passed arguments, keywords in incoming things'''

    def invoke(name):
        '''
        invoke method `name` on each incoming thing with passed arguments,
        keywords but return incoming thing instead if method returns `None`

        @param name: name of method
        '''

    def items():
        '''invoke call on each mapping to get key, value pairs'''

    def map():
        '''invoke call on each incoming thing'''

    def starmap():
        '''invoke call on each sequence of incoming things'''
