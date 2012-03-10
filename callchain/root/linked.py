# -*- coding: utf-8 -*-
'''active queued linked call chains'''

from callchain.mixin.active import (
    ActiveCallMixin, ActiveECallMixin, ActiveRootedMixin)
from callchain.assembly.linked import LinkedChain, Eventlink

from callchain.root.mixins import RootMixin


class chainlink(RootMixin, ActiveCallMixin, ActiveRootedMixin, LinkedChain):

    '''root linked chain'''


class eventlink(RootMixin, ActiveECallMixin, ActiveRootedMixin, Eventlink):

    '''root linked event chain'''
