# -*- coding: utf-8 -*-
'''active event chains'''

from callchain.chains.linked import ActiveLinkQMixin, LazyLinkQMixin

from callchain.events.core import ERunMixin, ERootedMixin

__all__ = ['ActiveELinkQMixin', 'LazyELinkQMixin']


class ActiveELinkQMixin(ERunMixin, ERootedMixin, ActiveLinkQMixin):

    '''active linked event chain mixin'''


class LazyELinkQMixin(ERunMixin, ERootedMixin, LazyLinkQMixin):

    '''lazy linked event chain mixin'''
