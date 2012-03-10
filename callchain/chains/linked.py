# -*- coding: utf-8 -*-
'''callchain linked call chains'''

from callchain.octopus import Tentacle

from callchain.chains.core import (
    ActiveMixin, LazyMixin, ActiveRootedQMixin, LazyRootedQMixin)

__all__ = ('ActiveLinkQMixin', 'LazyLinkQMixin', 'chainlink')


class ActiveLinkQMixin(ActiveRootedQMixin, ActiveMixin, Tentacle):

    '''active linked call chain queue mixin'''


class LazyLinkQMixin(LazyRootedQMixin, LazyMixin, Tentacle):

    '''lazy linked call chain queue mixin'''
