# -*- coding: utf-8 -*-'''call keys'''

from appspace.keys import Attribute

from callchain.keys.reset import KResetLocal


class KCall(KResetLocal):

    '''call key'''

    L = Attribute('local settings extracted')
    Meta = Attribute('local settings')
    port = Attribute('python 2.x <-> python 3.x porting helper')
    space = Attribute('external appspace interface')

    def __enter__():  # @NoSelf
        '''enter execution context'''

    def __exit__(e, t, b):  # @NoSelf
        '''exit execution context'''

    def switch(label, key=False):  # @NoSelf
        '''
        overt switch to linked chain configured in external appspace

        @param label: linked chain label
        @param key: linked chain chain key (default: False)
        '''

    def commit():  # @NoSelf
        '''consume call chain'''


class KEventCall(KCall):

    '''event call key'''

    def fire(*events):  # @NoSelf
        '''
        run calls bound to `events` **NOW**

        @param *events: event labels
        '''

    def queues(*events):  # @NoSelf
        '''
        ordered mapping of processing queues for `events`

        @param *events: event labels
        '''
