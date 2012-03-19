# -*- coding: utf-8 -*-
'''chain root chains appconf'''

from callchain.patterns import Pathways

__all__ = ['chain']


class chain(Pathways):
    chainlink = 'chain.root.chainlink.chainlink'


class event(Pathways):
    chainlink = 'chain.root.chainlink.eventlink'
    chain = 'chain.root.chainlink.chainlink'
