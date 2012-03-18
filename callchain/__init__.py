# -*- coding: utf-8 -*-
'''callchain: callables and components joined in one big happy chain'''

from callchain.chain import callchain, eventchain
from callchain.linked import chainlink, eventlink
from callchain.patterns import Pathways, Branchways, Nameways
from callchain.settings import DefaultSettings, RequiredSettings
from callchain.internal import ResetLocalMixin, ResetTypeMixin, inside, einside

__version__ = (0, 1, 3)
