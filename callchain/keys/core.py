# -*- coding: utf-8 -*-
'''callchain core keys'''

from appspace.keys import AppspaceKey, Attribute

__all__ = (
    'KSettings',  'KService', 'AChain', 'AChainlet', 'KRequired', 'KDefaults',
)


class KSettings(AppspaceKey):

    '''settings key'''


class KDefaults(AppspaceKey):

    '''default settings key'''


class KRequired(AppspaceKey):

    '''required settings key'''


class ACall(AppspaceKey):

    '''service key'''

    G = Attribute('application settings')
    L = Attribute('local manager settings')
    M = Attribute('external manager appspace')
    _G = Attribute('internal root settings')
    _M = Attribute('internal root appspace')
    space = Attribute('appspace')


class AChain(ACall):

    '''octopus key'''

    port = Attribute('python 2.x <-> python 3.x compatibility helper')


class AChainlet(ACall):

    '''tentacle key'''

    root = Attribute('root application')


class KService(AppspaceKey):

    '''service key'''


class NoServiceError(Exception):

    '''no service error'''
