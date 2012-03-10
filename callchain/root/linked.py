# -*- coding: utf-8 -*-
'''active queued linked call chains'''
from callchain.root.mixins import RootMixin
from callchain.assembly.linked import LinkedChain, Eventlink
from callchain.mixin.active import ActiveCallMixin, ActiveECallMixin


class chainlink(RootMixin, ActiveCallMixin, LinkedChain):

    '''root linked chain'''


class eventlink(RootMixin, ActiveECallMixin, Eventlink):

    '''root linked event chain'''
