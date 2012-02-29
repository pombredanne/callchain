# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''callchain core keys'''

from appspace.keys import AppspaceKey, Attribute

__all__ = (
    'ASettings', 'ADefaultSettings', 'ARequiredSettings', 'AService',
    'AOctopus', 'ATentacle',
)


class ASettings(AppspaceKey):

    '''settings key'''


class ADefaultSettings(AppspaceKey):

    '''default settings key'''


class ARequiredSettings(AppspaceKey):

    '''required settings key'''


class AService(AppspaceKey):

    '''service key'''
    
    G = Attribute('application settings')
    L = Attribute('local manager settings')
    M = Attribute('external manager appspace')
    _G = Attribute('internal root settings')
    _M = Attribute('internal root appspace')
    space = Attribute('appspace')

    def add(app, label, key=False):
        '''
        add application to appspace

        @param app: new application
        @param label: application label
        @param key: key label (default: False)
        '''
    
    def app(label, key=False):
        '''
        make application from appspace current call in chall chain

        @param label: application label
        @param key: key label (default: False)
        '''


class AOctopus(AService):

    '''octopus key'''
    
    port = Attribute('python 2.x <-> python 3.x compatibility helper')


class ATentacle(AService):

    '''tentacle key'''

    root = Attribute('root application')
