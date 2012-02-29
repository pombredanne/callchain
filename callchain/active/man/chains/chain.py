# -*- coding: utf-8 -*-
'''active manually balanced call chains'''

from twoq.active.mixins import AutoQMixin

from callchain.active.chains import AChainLinkMixin, ACallChainMixin

__all__ = ('callchain', 'chainlink')


class chainlink(AChainLinkMixin, AutoQMixin):

    '''manually balanced linked chain'''


class callchain(ACallChainMixin, AutoQMixin):

    '''manually balanced call chain'''
