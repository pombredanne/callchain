# -*- coding: utf-8 -*-
'''mapping services keys'''

from callchain.services.queue import KService


class KDelay(KService):

    '''delayed map key'''

    def delay_each(wait):  # @NoSelf
        '''
        invoke call with passed arguments, keywords in incoming things after
        delay `wait`

        @param wait: time in seconds
        '''

    def delay_invoke(name, wait):  # @NoSelf
        '''
        invoke method `name` on each incoming thing with passed arguments,
        keywords after delay `wait` but return incoming thing instead if method
        returns `None`

        @param name: name of method
        @param wait: time in seconds
        '''

    def delay_map(wait):  # @NoSelf
        '''
        invoke call on each incoming thing after delay `wait`

        @param wait: time in seconds
        '''


class KRepeat(KService):

    '''repetition key'''

    def copy():  # @NoSelf
        '''copy each incoming thing'''

    def padnone():  # @NoSelf
        '''repeat incoming things and then `None` indefinitely'''

    def range(start, stop=0, step=1):  # @NoSelf
        '''
        put sequence of numbers in incoming things

        @param start: number to start with
        @param stop: number to stop with (default: 0)
        @param step: number of steps to advance per iteration (default: 1)
        '''

    def repeat(n):  # @NoSelf
        '''
        repeat incoming things `n` times

        @param n: number of times to repeat
        '''

    def times(n=None):  # @NoSelf
        '''
        repeat call with incoming things `n` times

        @param n: repeat call n times on incoming things (default: None)
        '''


class KMap(KService):

    '''mapping key'''

    def map():  # @NoSelf
        '''invoke call on each incoming thing'''

    def invoke(name):  # @NoSelf
        '''
        invoke method `name` on each incoming thing with passed arguments,
        keywords but return incoming thing instead if method returns `None`

        @param name: name of method
        '''

    def each():  # @NoSelf
        '''invoke call with passed arguments, keywords in incoming things'''

    def starmap():  # @NoSelf
        '''invoke call on each sequence of incoming things'''

    def items():  # @NoSelf
        '''invoke call on each mapping to get key, value pairs'''
