# -*- coding: utf-8 -*-
'''callchain keys'''

from inspect import ismodule

from stuf.six import iteritems
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


class EFinally(EEvent):

    '''run anyway event key'''


###############################################################################
## call chains ################################################################
###############################################################################

class ARootChain(AppspaceKey):

    '''root call chain'''


class ABranchChain(AppspaceKey):

    '''branch call chain'''


class AEventChain(AppspaceKey):

    '''event call chain'''


__all__ = sorted(name for name, obj in iteritems(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
