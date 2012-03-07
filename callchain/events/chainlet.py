# -*- coding: utf-8 -*-
'''callchain eventlet mixins'''

from callchain.chains.chainlet import ActiveChainletQMixin, LazyChainletQMixin

from callchain.events.core import ERootedMixin, ECoreMixin

__all__ = ('ActiveELetQMixin', 'LazyELetQMixin')


class ActiveELetQMixin(ECoreMixin, ERootedMixin, ActiveChainletQMixin):

    '''active eventlet mixin'''


class LazyELetQMixin(ECoreMixin, ERootedMixin, LazyChainletQMixin):

    '''lazy eventlet mixin'''
