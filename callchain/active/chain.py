# -*- coding: utf-8 -*-
'''active queued call chains'''

from appspace.keys import appifies
from twoq.active.mixins import AutoResultMixin, ManResultMixin

from callchain.keys.apps import events
from callchain.keys.queue import KResults
from callchain.octopus import InsideMixin as inside
from callchain.chains import ChainQMixin, ChainMixin
from callchain.keys.chain import KEventChain, KCallChain
from callchain.events import inside as einside, EChainMixin

from callchain.active.apps import chain, event
from callchain.active.man.apps import chain as mchain
from callchain.active.auto.apps import chain as achain
from callchain.active.man.events import event as mevent
from callchain.active.auto.events import event as aevent
from callchain.active.mixins import ActiveMixin, ActiveEMixin, RootMixin


class ActiveChainMixin(ChainQMixin, ActiveMixin):

    '''active queued call chain mixin'''

    def __call__(self, *args):
        '''new chain session'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self._inextend(args)
        return self

    def back(self, link):
        '''
        handle chainlet end

        @param link: linked call chain
        '''
        self._cback(link)
        # sync with link incoming things
        self._inclear()
        self._inextend(link.incoming)
        # sync with link outgoing things
        self._outclear()
        self._outextend(link.outgoing)
        return self

    _ccback = back


class ActiveEChainMixin(ActiveEMixin, EChainMixin, ActiveChainMixin):

    '''active event chain mixin'''


#@appifies(KCallChain)
#@inside(chain)
#class callchain(RootMixin, ChainMixin, ActiveMixin):
#
#    '''call chain'''
#
#
#@appifies(KEventChain, KResults)
#@einside(event, events)
#class eventchain(EChainMixin, ActiveEMixin, callchain):
#
#    '''root event chain'''


@appifies(KCallChain, KResults)
@inside(achain)
class aachainq(ActiveChainMixin, AutoResultMixin):

    '''active queued auto-balancing call chain'''


@appifies(KEventChain, KResults)
@einside(aevent, events)
class aaeventq(ActiveEChainMixin, AutoResultMixin):

    '''active queued auto-balancing event chain'''


@appifies(KCallChain, KResults)
@inside(mchain)
class amchainq(ActiveChainMixin, ManResultMixin):

    '''active queued manually balanced call chain'''


@appifies(KEventChain, KResults)
@einside(mevent, events)
class ameventq(ActiveEChainMixin, ManResultMixin):

    '''active queued manually balanced event chain'''
