# -*- coding: utf-8 -*-
'''callchain: callables and components joined in one big happy callchain'''

from callchain.chain import inside, chainlink, callchain
from callchain.event import eventlink, eventchain, einside
from callchain.patterns import Pathways, Branchways, Nameways
from callchain.settings import DefaultSettings, RequiredSettings
from callchain.mixins.resets import ResetLocalMixin, ResetTypeMixin

__version__ = (0, 1, 3)
