# -*- coding: utf-8 -*-
'''active synchronized event chains'''

from twoq.active.mixins import SyncQMixin, SyncResultMixin

from callchain.active.events import LinkMixin, ChainMixin

__all__ = ['eventlink', 'eventchain']


class eventlink(LinkMixin, SyncQMixin):

    '''synchronized linked event chain'''


class eventchain(ChainMixin, SyncResultMixin):

    '''synchronized event chain'''
