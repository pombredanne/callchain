# -*- coding: utf-8 -*-
'''active queued linked call chains'''

from callchain.assembly.linked import LinkedChain, Eventlink

from callchain.root.mixins import RootMixin


class chainlink(RootMixin, LinkedChain):

    '''root linked chain'''


class eventlink(RootMixin, Eventlink):

    '''root linked event chain'''
