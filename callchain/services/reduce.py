# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''reducing service keys'''

from callchain.services.queue import KService


class KMath(KService):

    '''math mixin'''

    def average():
        '''average of all incoming things'''

    def fsum():
        '''add incoming things together'''

    def max():
        '''find maximum thing in incoming things using call as key function'''

    def median():
        '''mean of all incoming things'''

    def min():
        '''find minimum thing in incoming things using call as key function'''

    def minmax():
        '''minimum and maximum things among all incoming things'''

    def mode():
        '''mode of all incoming things'''

    def uncommon():
        '''least common incoming thing'''

    def frequency():
        '''frequency of each incoming thing'''

    def statrange():
        '''statistical range of all incoming things'''

    def sum(start=0):
        '''
        add all incoming things together

        @param start: starting number (default: 0)
        '''

class KTruth(KService):

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
        '''how many times call is `True` for incoming things'''


class KReduce(KService):

    '''reducing mixin'''

    def merge():
        '''flatten nested but ordered incoming things'''

    def smash():
        '''flatten deeply nested incoming things'''

    def pairwise():
        '''every two incoming things as a tuple'''

    def reduce(initial=None):
        '''
        reduce incoming things to one thing using call (from left side of
        incoming things)

        @param initial: initial thing (default: None)
        '''

    def reduce_right(initial=None):
        '''
        reduce incoming things to one thing from right side of incoming things
        using call

        @param initial: initial thing (default: None)
        '''

    def roundrobin():
        '''interleave incoming things into one thing'''

    def zip():
        '''
        smash incoming things into one single thing, pairing things by iterable
        position
        '''
