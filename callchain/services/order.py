# -*- coding: utf-8 -*-
'''ordering services keys'''

from callchain.services.queue import KService


class KRandom(KService):

    '''random key'''

    def choice():  # @NoSelf
        '''random choice of/from incoming things'''

    def sample(n):  # @NoSelf
        '''
        random sampling drawn from `n` incoming things

        @param n: number of incoming things
        '''

    def shuffle():  # @NoSelf
        '''randomly order incoming things'''


class KOrder(KService):

    '''ordering key'''

    def group():  # @NoSelf
        '''
        group incoming things, optionally using current call for key function
        '''

    def grouper(n, fill=None):  # @NoSelf
        '''
        split incoming things into sequences of length `n`, using `fill` thing
        to pad incomplete sequences

        @param n: number of things
        @param fill: fill thing (default: None)
        '''

    def reverse():  # @NoSelf
        '''reverse order of incoming things'''

    def sort():  # @NoSelf
        '''
        sort incoming things, optionally using current call as key function
        '''


class KCombine(KService):

    '''combination key'''

    def combinations(r):  # @NoSelf
        '''
        `r` length slices of incoming things

        @param r: length of combinations
        '''

    def permutations(r):  # @NoSelf
        '''
        successive `r` length permutations of incoming things

        @param r: length of permutations
        '''

    def product(n=1):  # @NoSelf
        '''
        nested for each loops repeated `n` times

        @param n: number of repetitions (default: 1)
        '''
