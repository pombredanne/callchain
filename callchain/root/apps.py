# -*- coding: utf-8 -*-
'''callchain root chains appconf'''

from callchain.patterns import Pathways

__all__ = ['chain']


class chain(Pathways):
    linked = 'callchain.root.linked.chainlink'


class event(Pathways):
    linked = 'callchain.root.linked.eventlink'
    callchain = 'callchain.root.linked.chainlink'
