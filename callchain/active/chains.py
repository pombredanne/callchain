# -*- coding: utf-8 -*-
'''callchain active call chains'''

from collections import deque

from twoq import twoq
from stuf.utils import iterexcept

from callchain.mixins.keys import ABranchChain
from callchain.mixins.chains import ChainsQMixin, BranchQMixin, ChainQMixin

__all__ = ['branchq', 'chainq']


class chainsq(ChainsQMixin, twoq):

    '''base call chain'''

    def __init__(self):
        super(chainsq, self).__init__()
        #######################################################################
        ## call chain #########################################################
        #######################################################################
        self._chain = deque()
        # call chain right extend
        self._cxtend = self._chain.extend
        # call chain right append
        self._cappendright = self._chain.append
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


class branchq(chainsq, BranchQMixin):

    '''call chain branch'''

    def __init__(self, root):
        super(branchq, self).__init__(root)
        # sync with root
        self.extend(root.outgoing)

    def back(self):
        '''return to root'''
        return self.root.clear().extend(self.outgoing)


class chainq(chainsq, ChainQMixin):

    '''root call chain'''

    def switch(self, label):
        '''
        switch to branch call chain

        @param label: chain label
        '''
        return self.M.ez_lookup(ABranchChain, label)(self)
