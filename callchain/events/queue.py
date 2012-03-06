# -*- coding: utf-8 -*-
'''active event chains'''

from callchain.chains.queue import (
    ActiveLinkMixin, ActiveChainMixin,  LazyLinkMixin, LazyChainMixin)

from callchain.events.mixins import ELinkMixin, EChainMixin


class ActiveEventLinkMixin(ELinkMixin, ActiveLinkMixin):

    '''active linked event chain mixin'''


class ActiveEventChainMixin(EChainMixin, ActiveChainMixin):

    '''active event chain mixin'''


class LazyEventLinkMixin(ELinkMixin, LazyLinkMixin):

    '''lazy linked event chain mixin'''


class LazyEventChainMixin(EChainMixin, LazyChainMixin):

    '''lazy event chain mixin'''
