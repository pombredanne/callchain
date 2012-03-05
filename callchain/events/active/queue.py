# -*- coding: utf-8 -*-
'''active event chains'''

from callchain.chains.active.queue import ChainLinkMixin, ChainMixin

from callchain.events.mixins import ELinkMixin, EChainMixin


class EventLinkMixin(ELinkMixin, ChainLinkMixin):

    '''active linked event chain mixin'''


class EventChainMixin(EChainMixin, ChainMixin):

    '''active event chain mixin'''
