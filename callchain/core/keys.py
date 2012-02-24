# -*- coding: utf-8 -*-
'''callchain core keys'''

from appspace.keys import AppspaceKey

__all__ = ('ASettings', 'ADefaultSettings', 'ARequiredSettings')


class ASettings(AppspaceKey):

    '''settings key'''


class ADefaultSettings(AppspaceKey):

    '''default settings key'''


class ARequiredSettings(AppspaceKey):

    '''required settings key'''
