# -*- coding: utf-8 -*-
'''callchain linked chain mixins'''

from callchain.call import CallMixin
from callchain.rooted import (
    RootedMixin, RootedQMixin, ERootedMixin, RootedChainMixin)


class Linked(CallMixin, RootedMixin):

    '''link chaining mixin'''


class LinkedChainMixin(CallMixin, RootedChainMixin):

    '''link chaining mixin'''


class LinkedQMixin(CallMixin, RootedQMixin):

    '''linked call chain mixin'''


class ELinkedMixin(CallMixin, ERootedMixin):

    '''linked linked event chain mixin'''
