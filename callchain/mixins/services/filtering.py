# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''filtering services keys'''

from appspace.keys import AppspaceKey


class SCollecting(AppspaceKey):

    '''collection key'''

    def deepmembers():
        '''collect object members from incoming things and their bases'''

    def members():
        '''collect object members from incoming things'''

    def pick(*names):
        '''collect object attributes from incoming things by their `*names`'''

    def pluck(*keys):
        '''collect object items from incoming things by item `*keys`'''


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
        '''


class SSlice(AppspaceKey):

    '''slicing key'''

    def nth(n, default=None):
        '''
        `nth` incoming thing or default thing

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


class SFilterMixin(SCollecting, SSet, SSlice):

    '''filter key'''

    def compact():
        '''strip "untrue" things from incoming things'''

    def filter():
        '''incoming things for which call is `True`'''

    def find():
        '''first incoming thing for which call is `True`'''

    def partition():
        '''
        split incoming things into `True` and `False` things based on results
        of call
        '''

    def reject():
        '''incoming things for which call is `False`'''

    def without(*things):
        '''strip things from incoming things'''
