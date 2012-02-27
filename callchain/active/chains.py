# -*- coding: utf-8 -*-
'''active call chains'''

from threading import local

from inspect import ismodule
from collections import deque

from stuf.six import items
from stuf.utils import iterexcept
from twoq.active.queuing import AutoQMixin, ManQMixin, SyncQMixin

from callchain.mixins.chains import ChainLinkMixin, CallChainMixin

###############################################################################
## active CallChain mixins ####################################################
###############################################################################


class AChainsMixin(local):

    '''base call chain'''

    def __init__(self):
        super(AChainsMixin, self).__init__()
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


class AChainLinkMixin(AChainsMixin, ChainLinkMixin):

    '''linked call chain mixin'''

    def __init__(self, root):
        super(AChainLinkMixin, self).__init__(root)
        # sync with root
        self.extend(root.outgoing)

    def back(self):
        '''return to root'''
        return self.root.clear().extend(self.outgoing)


class ACallChainMixin(AChainsMixin, CallChainMixin):

    '''call chain mixin'''

###############################################################################
## active link call chains ####################################################
###############################################################################


class AChainLink(AChainLinkMixin, AutoQMixin):

    '''auto-balancing link call chain'''

ChainLink = AChainLink


class MChainLink(AChainLinkMixin, ManQMixin):

    '''manually balanced link call chain'''


class SChainLink(ACallChainMixin, SyncQMixin):

    '''synchronized link call chain'''


###############################################################################
## active call chains #########################################################
###############################################################################


class ACallChain(ACallChainMixin, AutoQMixin):

    '''auto-balancing call chain'''

CallChain = ACallChain


class MCallChain(ACallChainMixin, ManQMixin):

    '''manually balanced call chain'''


class SCallChain(ACallChainMixin, SyncQMixin):

    '''synchronized call chain'''


__all__ = sorted(name for name, obj in items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
