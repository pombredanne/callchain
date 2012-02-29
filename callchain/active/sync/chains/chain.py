# -*- coding: utf-8 -*-
'''active synchronized call chains'''

from twoq.active.mixins import AutoQMixin

from callchain.active.chains import AChainLinkMixin, ACallChainMixin

__all__ = ('callchain', 'chainlink')


class chainlink(AChainLinkMixin, AutoQMixin):

    '''synchronized linked chain'''


class callchain(ACallChainMixin, AutoQMixin):

    '''synchronized call chain'''
