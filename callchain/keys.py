# -*- coding: utf-8 -*-
'''callchain keys'''

from appspace.keys import AppspaceKey

__all__ = (
    'ASettings', 'ADefaultSettings', 'ARequiredSettings', 'AEvent', 'AAll',
    'AChange', 'AInvoke', 'AProblem',
)

###############################################################################
## settings keys ##############################################################
###############################################################################


class ASettings(AppspaceKey):

    '''settings key'''


class ADefaultSettings(AppspaceKey):

    '''default settings key'''


class ARequiredSettings(AppspaceKey):

    '''required settings key'''


###############################################################################
## events #####################################################################
###############################################################################

class AEvent(AppspaceKey):

    '''event key'''


class AAll(AEvent):

    '''all event key'''


class AChange(AEvent):

    '''changes event key'''


class AInvoke(AEvent):

    '''invocation event key'''


class AProblem(AEvent):

    '''problem event key'''
