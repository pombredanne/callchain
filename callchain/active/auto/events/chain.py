# -*- coding: utf-8 -*-
'''active auto-balancing event chains'''

from twoq.active.mixins import AutoQMixin

from callchain.active.mixins.events import AEventLinkMixin, AEventChainMixin

__all__ = ['eventlink', 'eventchain']


class eventlink(AEventLinkMixin, AutoQMixin):

    '''auto-balancing linked event chain'''


class eventchain(AEventChainMixin, AutoQMixin):

    '''auto-balancing event chain'''
