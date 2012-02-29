# -*- coding: utf-8 -*-
'''active manually balanced event chains'''

from twoq.active.mixins import AutoQMixin

from callchain.active.events import AEventLinkMixin, AEventChainMixin

__all__ = ['eventlink', 'eventchain']


class eventlink(AEventLinkMixin, AutoQMixin):

    '''manually balanced linked event chain'''


class eventchain(AEventChainMixin, AutoQMixin):

    '''manually balanced event chain'''
