# -*- coding: utf-8 -*-
'''process events'''

from inspect import ismodule

from twoq import port

from callchain.mixins.events.events import EEvent


class ACreate(EEvent):

    '''create event marker'''


class ADelete(EEvent):

    '''delete event marker'''


class AExport(EEvent):

    '''export event marker'''


class AModify(EEvent):

    '''modification event'''


class APrepare(EEvent):

    '''prepare event marker'''


class ASync(EEvent):

    '''synchronization event marker'''


class AUpdate(EEvent):

    '''update event marker'''


__all__ = sorted(name for name, obj in port.items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
