# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
#pylint: disable-msg=e0211,e0213
'''manager keys'''

from appspace.keys import AppspaceKey, Attribute


class KConfig(AppspaceKey):

    '''configuration access key'''

    defaults = Attribute('default settings by their lonesome')
    required = Attribute('required settings by their lonesome')
    G = Attribute('external application global settings')


class KManager(KConfig):

    '''chain manager key'''

    def __init__(pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''

class KEventManager(KConfig):

    '''event manager key'''

    def __init__(
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
