# -*- coding: utf-8 -*-
'''filtering services keys'''

from callchain.services.queue import KService


class KCollect(KService):

    '''collection key'''

    def deepmembers():  # @NoSelf
        '''collect object members from incoming things and their bases'''

    def members():  # @NoSelf
        '''collect object members from incoming things'''

    def pick(*names):  # @NoSelf
        '''collect object attributes from incoming things by their `*names`'''

    def pluck(*keys):  # @NoSelf
        '''collect object items from incoming things by item `*keys`'''


class KSet(KService):

    '''set uniqueness key'''

    def difference():  # @NoSelf
        '''difference between incoming things'''

    def symmetric_difference():  # @NoSelf
        '''symmetric difference between incoming things'''

    def disjointed():  # @NoSelf
        '''disjoint between incoming things'''

    def intersection():  # @NoSelf
        '''intersection between incoming things'''

    def subset():  # @NoSelf
        '''incoming things that are subsets of incoming things'''

    def superset():  # @NoSelf
        '''incoming things that are supersets of incoming things'''

    def union():  # @NoSelf
        '''union between incoming things'''

    def unique():  # @NoSelf
        '''
        list unique incoming things, preserving order and remember all incoming
        things ever seen
        '''


class KSlice(KService):

    '''slicing key'''

    def nth(n, default=None):  # @NoSelf
        '''
        `nth` incoming thing or default thing

        @param n: number of things
        @param default: default thing (default: None)
        '''

    def initial():  # @NoSelf
        '''all incoming things except the last thing'''

    def rest():  # @NoSelf
        '''all incoming things except the first thing'''

    def snatch(n):  # @NoSelf
        '''
        last `n` things of incoming things

        @param n: number of things
        '''

    def take(n):  # @NoSelfs
        '''
        first `n` things of incoming things

        @param n: number of things
        '''


class KFilter(KService):

    '''filter key'''

    def compact():  # @NoSelf
        '''strip "untrue" things from incoming things'''

    def filter():  # @NoSelf
        '''incoming things for which call is `True`'''

    def find():  # @NoSelf
        '''first incoming thing for which call is `True`'''

    def partition():  # @NoSelf
        '''
        split incoming things into `True` and `False` things based on results
        of call
        '''

    def reject():  # @NoSelf
        '''incoming things for which call is `False`'''

    def without(*things):  # @NoSelf
        '''strip things from incoming things'''
