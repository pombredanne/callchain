# -*- coding: utf-8 -*-
'''callchain eventlets'''

from callchain.chains.chainlet import ActiveChainletQMixin, LazyChainletQMixin

from callchain.events.core import ERootedMixin

__all__ = ('ActiveELetQMixin', 'LazyELetQMixin')


class ActiveELetQMixin(ERootedMixin, ActiveChainletQMixin):

    '''active eventlet mixin'''


class LazyELetQMixin(ERootedMixin, LazyChainletQMixin):

    '''lazy eventlet mixin'''
