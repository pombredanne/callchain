# -*- coding: utf-8 -*-
'''callchain core keys'''

from appspace.keys import AppspaceKey

__all__ = (
    'KSettings',  'KService', 'AChain', 'AChainlet', 'KRequired', 'KDefaults',
)


class KSettings(AppspaceKey):

    '''settings key'''


class KDefaults(AppspaceKey):

    '''default settings key'''


class KRequired(AppspaceKey):

    '''required settings key'''


class KService(AppspaceKey):

    '''service key'''


class NoServiceError(Exception):

    '''no service error'''
