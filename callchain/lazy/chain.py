# -*- coding: utf-8 -*-
'''lazy queued call and event chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoResultMixin, ManResultMixin

from callchain.keys.apps import events
from callchain.keys.queue import KResults
from callchain.internal import inside, einside
from callchain.chain import ChainQ, EventChainQ

from callchain.lazy.mixins import LazyContextMixin
from callchain.lazy.man.apps import chain as mchain
from callchain.lazy.auto.apps import chain as achain
from callchain.lazy.man.events import event as mevent
from callchain.lazy.auto.events import event as aevent


@appifies(KResults)
class LazyChain(ChainQ, LazyContextMixin):

    '''lazy call chain'''


@inside(achain)
class lachainq(ChainQ, AutoResultMixin):

    '''lazy queued auto-balancing call chain'''


@inside(mchain)
class lmchainq(ChainQ, ManResultMixin):

    '''lazy queued manually balanced call chain'''


@appifies(KResults)
@einside(mevent, events)
class LazyEvent(EventChainQ, LazyContextMixin):

    '''lazy event chain'''


@einside(aevent, events)
class laeventq(EventChainQ, AutoResultMixin):

    '''lazy queued auto-balancing event chain'''


@einside(mevent, events)
class lmeventq(EventChainQ, ManResultMixin):

    '''lazy queued manually balanced event chain'''
