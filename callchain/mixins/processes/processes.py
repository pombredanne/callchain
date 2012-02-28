# -*- coding: utf-8 -*-
'''process keys'''

from inspect import ismodule

from twoq import port
from appspace.keys import AppspaceKey


class PProcess(AppspaceKey):

    '''process marker'''


class PAbort(PProcess):

    '''abort event key'''


class PAfter(PProcess):

    '''after event key'''


class PAnyway(PProcess):

    '''anyway event key'''


class PBefore(PProcess):

    '''before event key'''


class PWork(PProcess):

    '''work event key'''


__all__ = sorted(name for name, obj in port.items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
