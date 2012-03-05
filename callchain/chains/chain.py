# -*- coding: utf-8 -*-
'''call chains core'''

from collections import deque

from callchain.chains.mixins import BaseMixin, LinkMixin, ChainMixin

__all__ = ('chainlink', 'callchain')


class ChainAloneMixin(BaseMixin):

    def clear(self):
        '''clear every thing'''
        self._outclear()
        self._cclear()
        return self

    _cclear = clear


class chainlink(ChainAloneMixin, LinkMixin):

    '''linked call chain'''


class callchain(ChainAloneMixin, ChainMixin):

    '''call chain'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(callchain, self).__init__(pattern, required, defaults, **kw)
        self._setup_chain(deque())
        # outgoing things right extend
        self._outextend = self.outgoing.extend
        # outgoing things clear
        self._outclear = self.outgoing.clear
