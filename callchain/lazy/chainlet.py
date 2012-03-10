# -*- coding: utf-8 -*-
'''lazy queued chainlets'''

from callchain.assembly.chainlet import Eventlet, CallChainlet

from callchain.lazy.mixins import LazyRootedMixin


class LazyCallChainletMixin(CallChainlet, LazyRootedMixin):

    '''lazy call chainlet mixin'''


class LazyEventletMixin(Eventlet, LazyRootedMixin):

    '''lazy eventlet mixin'''
