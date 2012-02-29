# -*- coding: utf-8 -*-
'''manually balanced mapping linked event chains'''

from twoq.mixins.mapping import DelayMixin, CopyMixin, RepeatMixin, MapMixin

from twoq.active.mixins import AutoQMixin

from callchain.active.events import AEventLinkMixin

__all__ = ('delayevent', 'copyevent', 'repeatevent', 'mapevent')


class delayevent(AEventLinkMixin, AutoQMixin, DelayMixin):

    '''manually balanced delayed mapping linked event chain'''


class copyevent(AEventLinkMixin, AutoQMixin, CopyMixin):

    '''manually balanced copy linked event chain'''


class repeatevent(AEventLinkMixin, AutoQMixin, RepeatMixin):

    '''manually balanced repeat linked event chain'''


class mapevent(AEventLinkMixin, AutoQMixin, MapMixin):

    '''manually balanced mapping linked event chain'''
