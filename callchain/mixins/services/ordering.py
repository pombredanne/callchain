# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''ordering services keys'''

from appspace.keys import AppspaceKey


class SOrdering(AppspaceKey):

    '''order key'''

    def group():
        '''group incoming things using _call for key function'''

    def grouper(n, fill=None):
        '''
        split incoming things into sequences of length `n`, using fill thing to
        pad out incomplete sequences

        @param n: number of things
        @param fill: fill thing (default: None)

        grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
        '''

    def reverse():
        '''reverse incoming things'''

    def sort():
        '''sort incoming things using call for key function'''


class SRandom(AppspaceKey):

    '''random key'''

    def choice():
        '''random choice from incoming things'''

    def sample(n):
        '''
        random sampling drawn from `n` incoming things

        @param n: number of things
        '''

    def shuffle():
        '''shuffle incoming things'''


class SOrder(SOrdering, SRandom):

    '''ordering key'''
