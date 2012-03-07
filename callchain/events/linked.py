# -*- coding: utf-8 -*-
'''callchain linked event chain mixins'''

from callchain.chains.linked import ActiveLinkQMixin, LazyLinkQMixin

from callchain.events.core import ERootedMixin, EActiveMixin, ELazyMixin

__all__ = ['ActiveELinkQMixin', 'LazyELinkQMixin']


class ActiveELinkQMixin(EActiveMixin, ERootedMixin, ActiveLinkQMixin):

    '''active linked event chain mixin'''


class LazyELinkQMixin(ELazyMixin, ERootedMixin, LazyLinkQMixin):

    '''lazy linked event chain mixin'''
