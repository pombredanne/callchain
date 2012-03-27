# -*- coding: utf-8 -*-
'''root chain keys'''

from appspace.keys import Attribute

from callchain.keys.reset import KResetLocal


class KConfig(KResetLocal):

    '''configuration access key'''

    defaults = Attribute('default settings by their lonesome')
    required = Attribute('required settings by their lonesome')
    G = Attribute('external application global settings')


class KRoot(KConfig):

    '''root chain key'''

    def __init__(pattern=None, required=None, defaults=None, **kw):  # @NoSelf
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''

    def __call__(*args):  # @NoSelf
        '''new chain session'''

    def back(branch):  # @NoSelf
        '''
        handle return from branch chain

        @param branch: branch chain
        '''


class KEventRoot(KRoot):

    '''root event key'''

    def __init__(  # @NoSelf
        patterns=None,
        events=None,
        required=None,
        defaults=None,
        *args,
        **kw
    ):
        '''
        init

        @param patterns: pattern config or eventspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''

    def event(event):  # @NoSelf
        '''
        create or fetch `event`

        @param event: event label
        '''

    def unevent(event):  # @NoSelf
        '''
        drop `event`

        @param event: event label
        '''
