# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''filtering services keys'''

from callchain.services.queue import KService


class KCollect(KService):

    '''collection key'''

    def deepmembers():
        '''collect object members from incoming things and their bases'''

    def members():
        '''collect object members from incoming things'''

    def pick(*names):
        '''collect object attributes from incoming things by their `*names`'''

    def pluck(*keys):
        '''collect object items from incoming things by item `*keys`'''


class KSet(KService):

    '''set uniqueness key'''

    def difference():
        '''difference between incoming things'''
        
    def symmetric_difference():
        '''symmetric difference between incoming things'''

    def disjointed():
        '''disjoint between incoming things'''

    def intersection():
        '''intersection between incoming things'''
        
    def subset():
        '''incoming things are subsets of incoming things'''

    def superset():
        '''incoming things are supersets of incoming things'''

    def union():
        '''union between incoming things'''

    def unique():
        '''
        list unique incoming things, preserving order and remember all incoming
        things ever seen
        '''


class KSlice(KService):

    '''slicing key'''

    def nth(n, default=None):
        '''
        `nth` incoming thing or default thing

        @param n: number of things
        @param default: default thing (default: None)
        '''

    def initial():
        '''all incoming things except the last thing'''

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


class KFilter(KService):

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
