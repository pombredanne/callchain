# -*- coding: utf-8 -*-
'''callchain: callables and components joined in one big happy callchain'''

from callchain.internal import inside, einside
from callchain.chain import callchain, eventchain
from callchain.linked import chainlink, eventlink
from callchain.patterns import Pathways, Branchways, Nameways
from callchain.settings import DefaultSettings, RequiredSettings
from callchain.mixins.resets import ResetLocalMixin, ResetTypeMixin

__version__ = (0, 1, 3)
