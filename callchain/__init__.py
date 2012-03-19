# -*- coding: utf-8 -*-
'''callchain: callables and components joined in one big happy chain'''

from callchain.internal import inside, einside
from callchain.chain import callchain, eventchain
from callchain.linked import chainlink, eventlink
from callchain.resets import ResetLocalMixin, ResetTypeMixin
from callchain.patterns import Pathways, Branchways, Nameways
from callchain.settings import DefaultSettings, RequiredSettings

__version__ = (0, 1, 3)
