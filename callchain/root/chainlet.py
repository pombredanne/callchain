# -*- coding: utf-8 -*-
'''root chainlets'''

from appspace.keys import appifies

from callchain.keys.chain import KCallChain, KEventChain
from callchain.assembly.chainlet import Chainlet, Eventlet

from callchain.root.mixins import RootableMixin


@appifies(KCallChain)
class chainlet(RootableMixin, Chainlet):

    '''root call chainlet'''


@appifies(KEventChain)
class eventlet(RootableMixin, Eventlet):

    '''root eventlet'''
