# -*- coding: utf-8 -*-
'''callchain root event chains appconf'''

from callchain.octopus import Pathways

__all__ = ['event']


class event(Pathways):
    linked = 'callchain.events.root.linked.linkq'
    callchain = 'callchain.chains.root.linked.chainlink'
