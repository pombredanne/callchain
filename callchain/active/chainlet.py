# -*- coding: utf-8 -*-
'''active queued chainlets'''

from callchain.assembly.chainlet import Eventlet, CallChainlet

from callchain.mixin.active import ActiveRootedMixin


class ActiveCallChainletMixin(CallChainlet, ActiveRootedMixin):

    '''active call chainlet mixin'''


class ActiveEventletMixin(Eventlet, ActiveRootedMixin):

    '''active eventlet mixin'''
