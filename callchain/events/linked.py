# -*- coding: utf-8 -*-
'''active event chains'''

from callchain.chains.linked import ActiveLinkQMixin, LazyLinkQMixin

from callchain.events.core import (
    ERootedMixin, ECoreMixin, EActiveMixin, ELazyMixin)

__all__ = ['ActiveELinkQMixin', 'LazyELinkQMixin']


class ActiveELinkQMixin(
    ECoreMixin, EActiveMixin, ERootedMixin, ActiveLinkQMixin
):

    '''active linked event chain mixin'''


class LazyELinkQMixin(ECoreMixin, ELazyMixin, ERootedMixin, LazyLinkQMixin):

    '''lazy linked event chain mixin'''
