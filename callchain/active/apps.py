# -*- coding: utf-8 -*-
'''callchain root chains appconf'''

from callchain.patterns import Pathways

__all__ = ['chain']


class chain(Pathways):
    linked = 'callchain.active.linked.chainlink'


class event(Pathways):
    linked = 'callchain.active.linked.eventlink'
    callchain = 'callchain.active.linked.chainlink'
