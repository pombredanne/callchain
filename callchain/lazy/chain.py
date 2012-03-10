# -*- coding: utf-8 -*-
'''lazy queued call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import AutoResultMixin, ManResultMixin

from callchain.keys.apps import events
from callchain.keys.queue import KResults
from callchain.internal import inside, einside
from callchain.mixin.reset import ResetLocalMixin
from callchain.keys.chain import KCallChain, KEventChain
from callchain.assembly.chain import CallChainQ, EventChainQ

from callchain.lazy.man.apps import chain as mchain
from callchain.lazy.auto.apps import chain as achain
from callchain.lazy.man.events import event as mevent
from callchain.lazy.auto.events import event as aevent
from callchain.lazy.mixins import LazyCallMixin, LazyECallMixin


class LazyChainMixin(ResetLocalMixin):

    '''lazy queued chain mixin'''

    def __call__(self, *args):
        '''new chain session'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self.incoming = iter([args[0]]) if len(args) == 1 else iter(args)
        return self

    def back(self, link):
        '''
        handle chainlet end

        @param link: linked call chain
        '''
        self._qback(link)
        # sync with link incoming things
        self.incoming = link.incoming
        # sync with link outgoing things
        self.outgoing = link.outgoing
        return self

    _ccback = back


class LazyCallChainMixin(LazyCallMixin, LazyChainMixin, CallChainQ):

    '''lazy call chain mixin'''


@appifies(KCallChain, KResults)
@inside(achain)
class lachainq(LazyCallChainMixin, AutoResultMixin):

    '''lazy queued auto-balancing call chain'''


@appifies(KCallChain, KResults)
@inside(mchain)
class lmchainq(LazyCallChainMixin, ManResultMixin):

    '''lazy queued manually balanced call chain'''


class LazyEChainMixin(LazyECallMixin, LazyChainMixin, EventChainQ):

    '''lazy queued event chain mixin'''


@appifies(KEventChain, KResults)
@einside(aevent, events)
class laeventq(LazyEChainMixin, AutoResultMixin):

    '''lazy queued auto-balancing event chain'''


@appifies(KEventChain, KResults)
@einside(mevent, events)
class lmeventq(LazyEChainMixin, ManResultMixin):

    '''lazy queued manually balanced event chain'''
