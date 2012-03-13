# -*- coding: utf-8 -*-
'''root chainlets'''

from appspace.keys import appifies

from callchain.mixin.rooted import (
    RootletMixin, ChainRootedMixin, EventRootedMixin)
from callchain.keys.chain import KCallChain, KEventChain
from callchain.mixin.fluent import ChainMixin, EventMixin

from callchain.root.mixins import RootMixin


@appifies(KCallChain)
class chainlet(RootMixin, RootletMixin, ChainRootedMixin, ChainMixin):

    '''call chain'''


@appifies(KEventChain)
class eventlet(RootMixin, EventRootedMixin, RootletMixin, EventMixin):

    '''event chain'''
