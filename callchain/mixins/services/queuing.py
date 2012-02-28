# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''twoq queuing mixins'''

from appspace.keys import AppspaceKey


class Queueing(AppspaceKey):

    '''queuing key'''

    def args(*args, **kw):
        '''arguments for current callable'''

    def tap(call):
        '''
        add call

        @param call: a call
        '''

    def detap():
        '''clear call'''

    def wrap(call):
        '''build factory callable and make call'''

    def unwrap():
        '''clear call'''
        
    def ahead(n=None):
        '''
        move iterator n-steps ahead or, if n is `None`, consume entirely

        @param n: number of steps to advance (default: None)
        '''
