# -*- coding: utf-8 -*-
'''event keys'''

from inspect import ismodule

from stuf.six import items
from appspace.keys import AppspaceKey


###############################################################################
## events #####################################################################
###############################################################################

class EEvent(AppspaceKey):

    '''event key'''


class EBefore(EEvent):

    '''before event key'''


class EWork(EEvent):

    '''work event key'''


class EChange(EEvent):

    '''change event key'''


class EAny(EEvent):

    '''any events key'''


class EAfter(EEvent):

    '''after event key'''


class EProblem(EEvent):

    '''problem event key'''


class EAnyway(EEvent):

    '''run anyway event key'''


__all__ = sorted(name for name, obj in items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
