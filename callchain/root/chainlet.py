# -*- coding: utf-8 -*-
'''active chainlets'''

from callchain.mixin.active import ActiveRootedMixin
from callchain.assembly.chainlet import Eventlet, CallChainlet

from callchain.root.mixins import RootMixin


class chainlet(CallChainlet, ActiveRootedMixin, RootMixin):

    '''root call chainlet'''


class eventlet(Eventlet, ActiveRootedMixin, RootMixin):

    '''root event chainlet'''
