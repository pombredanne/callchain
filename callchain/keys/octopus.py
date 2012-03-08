# -*- coding: utf-8 -*-
'''callchain octopus keys'''

from appspace.keys import AppspaceKey, Attribute

__all__ = (
    'KSettings',  'KService', 'AOctopus', 'ATentacle', 'KRequired',
    'KDefaults',
)


class KSettings(AppspaceKey):

    '''settings key'''


class KDefaults(AppspaceKey):

    '''default settings key'''


class KRequired(AppspaceKey):

    '''required settings key'''


class AOctobase(AppspaceKey):

    '''service key'''

    G = Attribute('application settings')
    L = Attribute('local manager settings')
    M = Attribute('external manager appspace')
    _G = Attribute('internal root settings')
    _M = Attribute('internal root appspace')
    space = Attribute('appspace')


class AOctopus(AOctobase):

    '''octopus key'''

    port = Attribute('python 2.x <-> python 3.x compatibility helper')


class ATentacle(AOctobase):

    '''tentacle key'''

    root = Attribute('root application')


class KService(AppspaceKey):

    '''service key'''


class NoServiceError(Exception):

    '''no service error'''
