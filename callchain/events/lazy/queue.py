# -*- coding: utf-8 -*-
'''lazy event chains'''

from callchain.chains.lazy.queue import ChainLinkMixin, ChainMixin

from callchain.events.mixins import ELinkMixin, EChainMixin


class EventLinkMixin(ELinkMixin, ChainLinkMixin):

    '''lazy linked event chain mixin'''


class EventChainMixin(EChainMixin, ChainMixin):

    '''lazy event chain mixin'''
