# -*- coding: utf-8 -*-
'''callchain chains'''

from callchain.patterns import Pathways

from callchain.mixins.call import CallMixin
from callchain.mixins.core import ChainMixin
from callchain.mixins.root import RootMixin, ConfigMixin
from callchain.mixins.branch import BranchMixin, ChainletMixin, LinkedMixin


class inside(object):

    '''internal appspace configuration'''

    def __init__(self, pattern, required=None, defaults=None, *args, **kw):
        '''
        init

        @param pattern: pattern configuration class or appspace label
        @param required: required global settings (default: None)
        @param defaults: default global settings (default: None)
        '''
        self.pattern = pattern
        self.required = required
        self.defaults = defaults
        self.args = args
        self.kw = kw

    def __call__(self, that):
        # internal appspace manager
        that._M = Pathways.appspace(
            self.pattern,
            self.required,
            self.defaults,
            *self.args,
            **self.kw
        )
        # lock internal appspace global settings
        that._M.settings.lock()
        # set internal appspace global settings
        that._G = that._M.settings.final
        return that


class Chain(CallMixin, RootMixin, ChainMixin):

    '''call chain'''


class Linked(LinkedMixin, BranchMixin, ConfigMixin, CallMixin, ChainMixin):

    '''linked chain'''


class Chainlet(ChainletMixin, BranchMixin, ChainMixin):

    '''chainlet'''
