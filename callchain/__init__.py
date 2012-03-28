# -*- coding: utf-8 -*-
'''callchain: callables and components joined in one big happy callchain'''

from callchain.core import inside, einside
from callchain.resets import ResetLocalMixin, ResetTypeMixin
from callchain.patterns import Pathways, Branchways, Nameways
from callchain.settings import DefaultSettings, RequiredSettings
from callchain.active_auto.chain import (
    chainq as aachainq, callchain as aacallchain)
from callchain.active_auto.event import (
    eventq as aaeventq, eventchain as aaeventchain)
from callchain.active_man.chain import (
    chainq as amchainq, callchain as amcallchain)
from callchain.active_man.event import (
    eventq as ameventq, eventchain as ameventchain)
from callchain.lazy_auto.chain import (
    chainq as lachainq, callchain as lacallchain)
from callchain.lazy_auto.event import (
    eventq as laeventq, eventchain as laeventchain)
from callchain.lazy_man.chain import (
    chainq as lmchainq, callchain as lamcallchain)
from callchain.lazy_man.event import (
    eventq as lmeventq, eventchain as lmeventchain)

__version__ = (0, 2, 2)
