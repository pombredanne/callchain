# -*- coding: utf-8 -*-
'''octopus core keys'''

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


class AService(AppspaceKey):

    '''service key'''


class NoServiceError(Exception):

    '''no service error'''
