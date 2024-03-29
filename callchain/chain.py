# -*- coding: utf-8 -*-
'''callchain chains'''

from appspace.keys import appifies

from callchain.patterns import Pathways
from callchain.keys.chains import (
    KLinkedQ, KChain, KLinked, KChainlet, KChainletQ)

from callchain.mixins.call import CallMixin
from callchain.mixins.core import ChainMixin
from callchain.mixins.branch import (
    LitedMixin, BranchMixin, ChainletMixin, QBranchMixin, LinkedMixin)
from callchain.mixins.root import RootMixin, LiteMixin, QRootMixin, ConfigMixin

###############################################################################
## chain configuration ########################################################
###############################################################################


class chain(Pathways):
    link = 'callchain.chain.chainlink'


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

    _o_call = __call__

###############################################################################
## vanilla chain ##############################################################
###############################################################################


class Chain(CallMixin, RootMixin, ChainMixin):

    '''call chain'''


@appifies(KLinked)
class Linked(LinkedMixin, BranchMixin, ConfigMixin, CallMixin, ChainMixin):

    '''linked chain'''


@appifies(KChainlet)
class Chainlet(ChainletMixin, BranchMixin, ChainMixin):

    '''chainlet'''

###############################################################################
## vanilla queued chains ######################################################
###############################################################################


class ChainQ(QRootMixin, Chain):

    '''queued chain'''


@appifies(KLinkedQ)
class LinkedQ(QBranchMixin, Linked):

    '''queued linked chain'''


@appifies(KChainletQ)
class ChainletQ(QBranchMixin, Chainlet):

    '''queued chainlet'''

###############################################################################
## vanilla lite chains ########################################################
###############################################################################


@appifies(KChain)
@inside(chain)
class callchain(LiteMixin, Chain):

    '''lite chain'''


@appifies(KLinked)
class chainlink(LitedMixin, LiteMixin, Linked):

    '''lite linked chain'''


@appifies(KChainlet)
class chainlet(LitedMixin, Chainlet):

    '''lite chainlet'''
