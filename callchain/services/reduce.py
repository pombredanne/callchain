# -*- coding: utf-8 -*-
'''reducing service keys'''

from callchain.services.queue import KService


class KMath(KService):

    '''math key'''

    def average():  # @NoSelf
        '''average of all incoming things'''

    def fsum():  # @NoSelf
        '''add incoming things together'''

    def max():  # @NoSelf
        '''
        find maximum thing in incoming things, optionally using current
        call as key function
        '''

    def median():  # @NoSelf
        '''median of all incoming things'''

    def min():  # @NoSelf
        '''find minimum thing in incoming things using call as key function'''

    def minmax():  # @NoSelf
        '''minimum and maximum things among all incoming things'''

    def mode():  # @NoSelf
        '''mode of all incoming things'''

    def uncommon():  # @NoSelf
        '''least common incoming thing'''

    def frequency():  # @NoSelf
        '''frequency of each incoming thing'''

    def statrange():  # @NoSelf
        '''statistical range of all incoming things'''

    def sum(start=0):  # @NoSelf
        '''
        add all incoming things together

        @param start: starting number (default: 0)
        '''


class KTruth(KService):

    '''truth key'''

    def all():  # @NoSelf
        '''if `all` incoming things are `True`'''

    def any():  # @NoSelf
        '''if `any` incoming things are `True`'''

    def contains(thing):  # @NoSelf
        '''
        if `thing` is in incoming things

        @param thing: some thing
        '''

    def quantify():  # @NoSelf
        '''how many times call is `True` for incoming things'''


class KReduce(KService):

    '''reduce key'''

    def merge():  # @NoSelf
        '''flatten nested but ordered incoming things'''

    def smash():  # @NoSelf
        '''flatten deeply nested incoming things'''

    def pairwise():  # @NoSelf
        '''every two incoming things as a tuple'''

    def reduce(initial=None):  # @NoSelf
        '''
        reduce incoming things to one thing using call (from left side of
        incoming things)

        @param initial: initial thing (default: None)
        '''

    def reduce_right(initial=None):  # @NoSelf
        '''
        reduce incoming things to one thing from right side of incoming things
        using call

        @param initial: initial thing (default: None)
        '''

    def roundrobin():  # @NoSelf
        '''interleave incoming things into one thing'''

    def zip():  # @NoSelf
        '''
        smash incoming things into one single thing, pairing things by iterable
        position
        '''
