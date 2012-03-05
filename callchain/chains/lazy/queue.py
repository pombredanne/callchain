# -*- coding: utf-8 -*-
'''lazy call chain mixins'''

from callchain.chains.queue import LinkQMixin, ChainQMixin


class ChainLinkMixin(LinkQMixin):

    '''linked call chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        # sync with root incoming things
        self.incoming = root.incoming
        # sync with root outgoing things
        self.outgoing = root.outgoing
        super(ChainLinkMixin, self).__init__(root)


class ChainMixin(ChainQMixin):

    '''call chain mixin'''

    def __call__(self, *args):
        '''load args into incoming thing'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self.incoming = iter([args[0]]) if len(args) == 1 else iter(args)
        return self

    def back(self, link):
        '''
        return from linked call chain

        @param link: linked call chain
        '''
        self._cback(link)
        # sync with link incoming things
        self.incoming = link.incoming
        # sync with link outgoing things
        self.outgoing = link.outgoing
        return self

    _ccback = back
