# -*- coding: utf-8 -*-
'''active call chain mixins'''

from callchain.chains.mixins import LinkQMixin, ChainQMixin


class ChainLinkMixin(LinkQMixin):

    '''linked call chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(ChainLinkMixin, self).__init__(root)
        # sync with root incoming things
        self._inextend(root.incoming)
        # sync with root outgoing things
        self._outextend(root.outgoing)


class ChainMixin(ChainQMixin):

    '''call chain mixin'''

    def __call__(self, *args):
        '''load args into incoming thing'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self._inextend(args)
        return self

    def back(self, link):
        '''
        return from linked call chain

        @param link: linked call chain
        '''
        self._cback(link)
        # sync with link incoming things
        self._inclear()
        self._inextend(link.incoming)
        # sync with link outgoing things
        self._outclear()
        self._outextend(link.outgoing)
        return self

    _ccback = back
