# -*- coding: utf-8 -*-
'''lazy queued call chains'''

from appspace.keys import appifies
from twoq.lazy.mixins import ManResultMixin,  AutoResultMixin

from callchain.keys.apps import events
from callchain.chain import ChainQMixin, EChainMixin
from callchain.keys.queue import KResults
from callchain.internal import inside, einside
from callchain.keys.chain import KCallChain, KEventChain

from callchain.lazy.man.apps import chain as mchain
from callchain.lazy.auto.apps import chain as achain
from callchain.lazy.man.events import event as mevent
from callchain.lazy.auto.events import event as aevent
from callchain.lazy.mixins import LazyMixin, LazyEMixin


class LazyChainMixin(LazyMixin, ChainQMixin):

    '''queued lazy call chain mixin'''

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
        self._cback(link)
        # sync with link incoming things
        self.incoming = link.incoming
        # sync with link outgoing things
        self.outgoing = link.outgoing
        return self

    _ccback = back


class LazyEChainMixin(LazyEMixin, EChainMixin, LazyChainMixin):

    '''lazy event chain mixin'''


@appifies(KCallChain, KResults)
@inside(achain)
class lachainq(LazyChainMixin, AutoResultMixin):

    '''lazy auto-balancing call chain'''


@appifies(KCallChain, KResults)
@inside(mchain)
class lmchainq(LazyChainMixin, ManResultMixin):

    '''lazy manually balanced call chain'''


@appifies(KEventChain, KResults)
@einside(aevent, events)
class laeventq(LazyEChainMixin, AutoResultMixin):

    '''lazy auto-balancing event chain'''


@appifies(KEventChain, KResults)
@einside(mevent, events)
class lmeventq(LazyEChainMixin, ManResultMixin):

    '''lazy manually balanced event chain'''
