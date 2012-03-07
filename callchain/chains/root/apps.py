# -*- coding: utf-8 -*-
'''callchain root chains appconf'''

from callchain.octopus import Pathways

__all__ = ['chain']


class chain(Pathways):
    linked = 'callchain.chains.root.linked.chainlink'
