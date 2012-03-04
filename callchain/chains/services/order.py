# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''ordering services keys'''

from appspace.keys import AppspaceKey


class KRandom(AppspaceKey):

    '''random key'''

    def choice():
        '''random choice of/from incoming things'''

    def sample(n):
        '''
        random sampling drawn from `n` incoming things

        @param n: number of incoming things
        '''

    def shuffle():
        '''randomly order incoming things'''


class KOrder(AppspaceKey):

    '''ordering key'''
    
    def group():
        '''group incoming things using call for key function'''

    def grouper(n, fill=None):
        '''
        split incoming things into sequences of length `n`, using `fill` thing
        to pad incomplete sequences

        @param n: number of things
        @param fill: fill thing (default: None)
        '''

    def reverse():
        '''reverse order of incoming things'''

    def sort():
        '''order incoming things using call for key function'''
