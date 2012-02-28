# -*- coding: utf-8 -*-
'''auto-balancing mapping linked event chains'''

from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from twoq.active.mixins import AutoQMixin

from callchain.active.mixins.events import AEventLinkMixin

__all__ = ('delayevent', 'copyevent', 'repeatevent', 'mapevent')


class delayevent(AEventLinkMixin, AutoQMixin, DelayMixin):

    '''auto-balancing delayed mapping linked event chain'''


class copyevent(AEventLinkMixin, AutoQMixin, CopyMixin):

    '''auto-balancing copy linked event chain'''


class repeatevent(AEventLinkMixin, AutoQMixin, RepeatMixin):

    '''auto-balancing repeat linked event chain'''


class mapevent(AEventLinkMixin, AutoQMixin, MapMixin):

    '''auto-balancing mapping linked event chain'''
