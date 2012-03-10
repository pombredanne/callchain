# -*- coding: utf-8 -*-
'''callchain: callables and components joined in one big happy chain'''

__version__ = (0, 1, 1)

from callchain.assembly.chain import Chain
from callchain.assembly.linked import Linked
from callchain.internal import inside, einside
from callchain.assembly.chainlet import Chainlet
from callchain.root.chain import callchain, eventchain
from callchain.root.linked import chainlink, eventlink
from callchain.patterns import Pathways, Branchways, Nameways
from callchain.settings import DefaultSettings, RequiredSettings
from callchain.lazy.chain import lmchainq, lmeventq, lachainq, laeventq
from callchain.active.chain import amchainq, ameventq, aachainq, aaeventq
