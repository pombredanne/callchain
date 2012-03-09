# -*- coding: utf-8 -*-
'''active chainlets'''

from callchain.active.mixins import RootMixin
from callchain.chainlet import (
    ChainletQMixin, EChainletMixin, ChainletCallMixin)


class ActiveChainletMixin(ChainletQMixin):

    '''active queue rooted chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(ActiveChainletMixin, self).__init__(root)
        # sync with root incoming things
        self._inextend(root.incoming)
        # sync with root outgoing things
        self._outextend(root.outgoing)


class ActiveEventletMixin(EChainletMixin, ActiveChainletMixin):

    '''active eventlet mixin'''


class chainlet(ChainletCallMixin, RootMixin):

    '''root chainlet'''


class eventlet(EChainletMixin, chainlet):

    '''root event chainlet'''
