# -*- coding: utf-8 -*-
'''event chains'''

from callchain.chains.chain import ChainAloneMixin

from callchain.events.mixins import EBaseMixin, ELinkMixin, EChainMixin

__all__ = ('eventchain', 'eventlink')


class _EventAloneMixin(EBaseMixin, ChainAloneMixin):

    '''standalone event chain mixin'''


class eventlink(_EventAloneMixin, ELinkMixin):

    '''linked event chain'''


class eventchain(_EventAloneMixin, EChainMixin):

    '''event chain'''
