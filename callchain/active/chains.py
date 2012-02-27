# -*- coding: utf-8 -*-
'''active call chains'''

from threading import local

from inspect import ismodule
from collections import deque

from stuf.six import items
from stuf.utils import iterexcept
from twoq.active.queuing import autoq, manq, syncq

from callchain.mixins.chains import LinkQMixin, ChainQMixin

###############################################################################
## active callchain mixins ####################################################
###############################################################################


class AChainsQMixin(local):

    '''base call chain'''

    def __init__(self):
        super(AChainsQMixin, self).__init__()
        ## call chain #########################################################
        self._chain = deque()
        # call chain right extend
        self._cxtend = self._chain.extend
        # call chain right append
        self._cappend = self._chain.append
        # call chain left append
        self._cappendleft = self._chain.appendleft
        # call chain left pop
        self._cpopleft = self._chain.popleft
        # call chain clear
        self._cclear = self._chain.clear

    def commit(self):
        '''invoke call chain'''
        # consume call chain until exhausted & put results in outgoing things
        calls = iterexcept(self._chain.popleft, IndexError)
        self.outappend(call() for call in calls)
        return self

    def chain(self, call, key=False, *args, **kw):
        '''
        add callable or appspaced application to call chain, partializing it
        with any passed parameters

        @param call: callable or application label
        @param key: key label (default: False)
        '''
        self._cappend(self.M.partial(call, key, *args, **kw))
        return self


class ALinkQMixin(AChainsQMixin, LinkQMixin):

    '''linked call chain mixin'''

    def __init__(self, root):
        super(ALinkQMixin, self).__init__(root)
        # sync with root
        self.extend(root.outgoing)

    def back(self):
        '''return to root'''
        return self.root.clear().extend(self.outgoing)


class AChainQMixin(AChainsQMixin, ChainQMixin):

    '''call chain mixin'''

###############################################################################
## active link call chains ####################################################
###############################################################################


class alinkq(ALinkQMixin, autoq):

    '''auto-balancing link call chain'''

linkq = alinkq


class mlinkq(ALinkQMixin, manq):

    '''manually balanced link call chain'''


class slinkq(AChainQMixin, syncq):

    '''synchronized link call chain'''


###############################################################################
## active call chains #########################################################
###############################################################################


class achainq(AChainQMixin, autoq):

    '''auto-balancing call chain'''

chainq = achainq


class mchainq(AChainQMixin, manq):

    '''manually balanced call chain'''


class schainq(AChainQMixin, syncq):

    '''synchronized call chain'''


__all__ = sorted(name for name, obj in items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
