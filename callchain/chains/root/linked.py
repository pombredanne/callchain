# -*- coding: utf-8 -*-
'''callchain root linked call chains'''

from callchain.octopus import Tentacle
from callchain.chains.core import ActiveMixin, RootedMixin

from callchain.chains.root.core import RootMixin

__all__ = ['chainlink']


class chainlink(RootMixin, RootedMixin, ActiveMixin, Tentacle):

    '''root linked call chain'''
