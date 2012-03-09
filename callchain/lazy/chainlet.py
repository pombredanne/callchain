# -*- coding: utf-8 -*-
'''lazy queued chainlets'''

from callchain.chainlet import EChainletMixin, ChainletQMixin


class LazyChainletMixin(ChainletQMixin):

    '''lazy queued rooted chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(LazyChainletMixin, self).__init__(root)
        # sync with root incoming things
        self.incoming = root.incoming
        # sync with root outgoing things
        self.outgoing = root.outgoing


class LazyEventletMixin(EChainletMixin, LazyChainletMixin):

    '''lazy eventlet mixin'''
