# -*- coding: utf-8 -*-
'''callchain root event chainlets'''

from callchain.events.core import ERootedMixin
from callchain.chains.root.chainlet import chainlet

__all__ = ['eventlet']


class eventlet(ERootedMixin, chainlet):

    '''root event chainlet'''
