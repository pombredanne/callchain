# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''reducing service keys'''

from appspace.keys import AppspaceKey


class Math(AppspaceKey):

    '''math mixin'''

    def average():
        '''average of all incoming things'''

    def fsum():
        '''
        add incoming things together

        @param start: starting number (default: 0)
        '''

    def max():
        '''find maximum value in incoming things using call for key function'''

    def median():
        '''mean of incoming things'''

    def min():
        '''find minimum value in incoming things using call for key function'''

    def minmax():
        '''minimum and maximum values among incoming things'''

    def mode():
        '''mode of incoming things'''

    def uncommon():
        '''least common incoming thing'''

    def frequency():
        '''frequency of each incoming thing'''

    def statrange():
        '''statistical range of incoming things'''

    def sum(start=0):
        '''
        add incoming things together

        @param start: starting number (default: 0)
        '''


class Reducing(AppspaceKey):

    '''reduce mixin'''

    def merge():
        '''flatten nested and ordered incoming things'''

    def smash(_smash=smash):
        '''flatten deeply nested incoming things'''

    def pairwise():
        '''
        every two incoming things as a tuple

        s -> (s0,s1), (s1,s2), (s2, s3), ...
        '''

    def reduce(initial=None):
        '''
        reduce incoming things to one thing using call

        @param initial: initial thing (default: None)
        '''

    def reduce_right(initial=None):
        '''
        reduce incoming things to one thing from right side using call

        @param initial: initial thing (default: None)
        '''

    def roundrobin():
        '''
        interleave incoming things into one thing e.g.

        roundrobin('ABC', 'D', 'EF') --> A D E B F C
        '''

    def zip():
        '''
        smash incoming things into single thing, pairing things by iterable
        position
        '''


class Truth(AppspaceKey):

    '''truth mixin'''

    def all():
        '''if `all` incoming things are `True`'''

    def any():
        '''if `any` incoming things are `True`'''

    def contains(thing):
        '''
        if `thing` is in incoming things

        @param thing: some thing
        '''

    def quantify():
        '''how many times call is True for incoming things'''


class Reduce(Math, Reducing, Truth):

    '''reducing mixin'''
