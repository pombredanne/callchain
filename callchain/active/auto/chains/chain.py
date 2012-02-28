# -*- coding: utf-8 -*-
'''active auto-balancing call chains'''

from twoq.active.mixins import AutoQMixin

from callchain.active.mixins.chains import AChainLinkMixin, ACallChainMixin

__all__ = ('callchain', 'chainlink')


class chainlink(AChainLinkMixin, AutoQMixin):

    '''auto-balancing linked chain'''


class callchain(ACallChainMixin, AutoQMixin):

    '''auto-balancing call chain'''
