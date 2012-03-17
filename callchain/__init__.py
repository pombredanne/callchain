# -*- coding: utf-8 -*-
'''callchain: callables and components joined in one big happy chain'''

__version__ = (0, 1, 2)

from callchain.internal import inside, einside
from callchain.root.chain import callchain, eventchain
from callchain.root.linked import chainlink, eventlink
from callchain.patterns import Pathways, Branchways, Nameways
from callchain.settings import DefaultSettings, RequiredSettings
from callchain.mixin.reset import ResetLocalMixin, ResetTypeMixin
from callchain.lazy.chain import lmchainq, lmeventq, lachainq, laeventq
from callchain.active.chain import amchainq, ameventq, aachainq, aaeventq
