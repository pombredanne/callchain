# -*- coding: utf-8 -*-
'''active synchronized call chains'''

from twoq.active.mixins import AutoQMixin

from callchain.active.chains import ChainLinkMixin, CallChainMixin

__all__ = ('callchain', 'chainlink')


class chainlink(ChainLinkMixin, AutoQMixin):

    '''synchronized linked chain'''


class callchain(CallChainMixin, AutoQMixin):

    '''synchronized call chain'''
