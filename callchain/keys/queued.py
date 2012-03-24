# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''queue keys'''

from callchain.keys.reset import KResetLocal


class KQueued(KResetLocal):

    '''queued key'''

    def clear():
        '''clear queues'''

    def tap(call, key=False):
        '''
        add call

        @param call: callable or appspace label
        @param key: appspace key (default: False)
        '''


class KQueuedRoot(KQueued):

    def back(branch):
        '''
        handle return from branch chain

        @param branch: branch chain
        '''
