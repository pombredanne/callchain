# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''filtering services keys'''

from appspace.keys import AppspaceKey


class SFiltering(AppspaceKey):

    '''filtering key'''

    def compact():
        '''strip "untrue" things from incoming things'''

    def filter():
        '''incoming things for which call is `True`'''

    def find():
        '''first incoming thing for which call is `True`'''

    def partition():
        '''
        split incoming things into `True` and `False` things based on results
        of callable

        @param test: a test
        '''

    def reject():
        '''incoming things for which call is `False`'''

    def without(*things):
        '''strip things from incoming things'''


class SCollecting(AppspaceKey):

    '''collection key'''

    def deepmembers():
        '''collect members of incoming things and their bases'''

    def members():
        '''collect members of incoming things'''

    def pick(*names):
        '''attributes of incoming things by attribute `*names`'''

    def pluck(*keys):
        '''items of incoming things by item `*keys`'''


class SSet(AppspaceKey):

    '''set uniqueness key'''

    def difference():
        '''difference between incoming things'''

    def intersection():
        '''intersection between incoming things'''

    def union():
        '''union between incoming things'''

    def unique():
        '''
        list unique incoming things, preserving order and remember all incoming
        things ever seen

        unique('AAAABBBCCDAABBB') --> A B C D
        unique('ABBCcAD', str.lower) --> A B C D
        '''


class SSlice(AppspaceKey):

    '''slicing key'''

    def nth(n, default=None):
        '''
        nth incoming thing or default thing

        @param n: number of things
        @param default: default thing (default: None)
        '''

    def initial():
        '''all incoming things except the last thing'''

    _oinitial = initial

    def rest():
        '''all incoming things except the first thing'''

    def snatch(n):
        '''
        last `n` things of incoming things

        @param n: number of things
        '''

    def take(n):
        '''
        first `n` things of incoming things

        @param n: number of things
        '''


class SFilterMixin(SFiltering, SCollecting, SSet, SSlice):

    '''filter key'''
