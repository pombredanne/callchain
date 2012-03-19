# -*- coding: utf-8 -*-
'''event keys'''

from appspace.keys import AppspaceKey


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
