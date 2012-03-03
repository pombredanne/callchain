# -*- coding: utf-8 -*-
'''active synchronized call chains'''

from twoq.active.mixins import AutoQMixin, AutoMixin

from callchain.active.chains import ChainLinkMixin, CallChainMixin

__all__ = ('callchain', 'chainlink')


class chainlink(ChainLinkMixin, AutoQMixin):

    '''synchronized linked chain'''


class callchain(CallChainMixin, AutoMixin):

    '''synchronized call chain'''
