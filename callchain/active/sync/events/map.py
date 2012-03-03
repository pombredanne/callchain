# -*- coding: utf-8 -*-
'''synchronized mapping linked event chains'''

from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from twoq.active.mixins import SyncQMixin

from callchain.active.events import LinkMixin

__all__ = ('delayevent', 'copyevent', 'repeatevent', 'mapevent')


class delayevent(LinkMixin, SyncQMixin, DelayMixin):

    '''synchronized delayed mapping linked event chain'''


class copyevent(LinkMixin, SyncQMixin, CopyMixin):

    '''synchronized copy linked event chain'''


class repeatevent(LinkMixin, SyncQMixin, RepeatMixin):

    '''synchronized repeat linked event chain'''


class mapevent(LinkMixin, SyncQMixin, MapMixin):

    '''synchronized mapping linked event chain'''
