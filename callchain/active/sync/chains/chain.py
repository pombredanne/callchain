# -*- coding: utf-8 -*-
'''active synchronized call chains'''

from twoq.active.mixins import SyncQMixin, SyncResultMixin

from callchain.active.chains import ChainLinkMixin, CallChainMixin

__all__ = ('callchain', 'chainlink')


class chainlink(ChainLinkMixin, SyncQMixin):

    '''synchronized linked chain'''


class callchain(CallChainMixin, SyncResultMixin):

    '''synchronized call chain'''
