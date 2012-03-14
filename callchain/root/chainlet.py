# -*- coding: utf-8 -*-
'''root chainlets'''

from appspace.keys import appifies

from callchain.keys.chain import KCallChain, KEventChain
from callchain.assembly.chainlet import CallChainlet, Eventlet

from callchain.root.mixins import RootMixin


@appifies(KCallChain)
class chainlet(RootMixin, CallChainlet):

    '''call chain'''


@appifies(KEventChain)
class eventlet(RootMixin, Eventlet):

    '''event chain'''
