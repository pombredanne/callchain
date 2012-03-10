# -*- coding: utf-8 -*-
'''active chainlets'''

from callchain.assembly.chainlet import Eventlet, CallChainlet

from callchain.root.mixins import RootMixin


class chainlet(CallChainlet, RootMixin):

    '''root call chainlet'''


class eventlet(Eventlet, RootMixin):

    '''root event chainlet'''
