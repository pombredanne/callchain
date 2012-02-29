# -*- coding: utf-8 -*-
'''synchronized mapping linked event chains'''

from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from twoq.active.mixins import AutoQMixin

from callchain.active.events import AEventLinkMixin

__all__ = ('delayevent', 'copyevent', 'repeatevent', 'mapevent')


class delayevent(AEventLinkMixin, AutoQMixin, DelayMixin):

    '''synchronized delayed mapping linked event chain'''


class copyevent(AEventLinkMixin, AutoQMixin, CopyMixin):

    '''synchronized copy linked event chain'''


class repeatevent(AEventLinkMixin, AutoQMixin, RepeatMixin):

    '''synchronized repeat linked event chain'''


class mapevent(AEventLinkMixin, AutoQMixin, MapMixin):

    '''synchronized mapping linked event chain'''
