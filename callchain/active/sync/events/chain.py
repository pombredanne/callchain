# -*- coding: utf-8 -*-
'''active synchronized event chains'''

from twoq.active.mixins import AutoQMixin, AutoMixin

from callchain.active.events import AEventLinkMixin, AEventChainMixin

__all__ = ['eventlink', 'eventchain']


class eventlink(AEventLinkMixin, AutoQMixin):

    '''synchronized linked event chain'''


class eventchain(AEventChainMixin, AutoMixin):

    '''synchronized event chain'''
