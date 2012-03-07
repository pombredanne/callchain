# -*- coding: utf-8 -*-
'''callchain root event chains'''

from callchain.chains.root.linked import chainlink
from callchain.events.core import ERootedMixin, EActiveMixin

__all__ = ['eventlink']


class eventlink(ERootedMixin, EActiveMixin, chainlink):

    '''root linked event chain'''
