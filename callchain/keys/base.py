# -*- coding: utf-8 -*-
'''callchain base keys'''

from appspace.keys import AppspaceKey

from callchain.keys.reset import KResetLocal


class KSettings(KResetLocal):

    '''settings key'''


class KDefaults(AppspaceKey):

    '''default settings key'''


class KRequired(AppspaceKey):

    '''required settings key'''


class NoServiceError(Exception):

    '''no service error'''
