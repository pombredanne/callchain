# -*- coding: utf-8 -*-
'''active event chains'''

from callchain.chains.linked import ActiveLinkQMixin, LazyLinkQMixin

from callchain.events.core import ERunMixin, ERootedMixin, ECoreMixin

__all__ = ['ActiveELinkQMixin', 'LazyELinkQMixin']


class ActiveELinkQMixin(ECoreMixin, ERunMixin, ERootedMixin, ActiveLinkQMixin):

    '''active linked event chain mixin'''


class LazyELinkQMixin(ECoreMixin, ERunMixin, ERootedMixin, LazyLinkQMixin):

    '''lazy linked event chain mixin'''
