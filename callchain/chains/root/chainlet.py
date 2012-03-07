# -*- coding: utf-8 -*-
'''callchain root call chainlets'''

from callchain.chains.core import RootedMixin
from callchain.chains.chainlet import ChainletMixin

from callchain.chains.root.core import RootMixin

__all__ = ['chainlet']


class chainlet(ChainletMixin, RootedMixin, RootMixin):

    '''root call chainlets'''
