# -*- coding: utf-8 -*-
'''callchain base keys'''

from appspace.keys import AppspaceKey


class KSettings(AppspaceKey):

    '''settings key'''


class KDefaults(AppspaceKey):

    '''default settings key'''


class KRequired(AppspaceKey):

    '''required settings key'''


class NoServiceError(Exception):

    '''no service error'''
