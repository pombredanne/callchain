# -*- coding: utf-8 -*-
'''callchain root call chains'''

from appspace.keys import appifies

from callchain.octopus.core import inside
from callchain.chains.core import ActiveMixin
from callchain.chains.chain import ChainMixin
from callchain.chains.keys.core import KCallChain

from callchain.chains.root.apps import chain
from callchain.chains.root.core import RootMixin

__all__ = ['callchain']


@appifies(KCallChain)
@inside(chain)
class callchain(RootMixin, ChainMixin, ActiveMixin):

    '''call chain'''
