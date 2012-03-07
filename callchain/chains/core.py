# -*- coding: utf-8 -*-
'''callchains chain mixins'''

from collections import deque
from functools import partial

from stuf.utils import iterexcept
from twoq.support import isstring

from callchain.octopus import ResetLocalMixin

__all__ = ('LoneMixin', 'QMixin')


class _CoreMixin(ResetLocalMixin):

    '''core chain mixin'''

    def _setup_chain(self):
        '''setup call chain'''
        _chain = deque()
        # call chain right extend
        self._cxtend = _chain.extend
        # call chain right append
        self._cappend = _chain.append
        # call chain left append
        self._cappendleft = _chain.appendleft
        # call chain left pop
        self._cpopleft = _chain.popleft
        # call chain clear
        self._cclear = _chain.clear
        # call chain
        self._chain = _chain

    _osetup_chain = _setup_chain

    def chain(self, call, key=False, *args, **kw):
        '''
        add callable or appspaced callable to call chain, partializing it with
        any passed arguments

        @param call: callable or application label
        @param key: appspace key label (default: False)
        '''
        if not isstring(call):
            call = partial(call, *(key,) + args, **kw)
        else:
            call = partial(self.M.get(call, key), *args, **kw)
        self._cappend(call)
        return self

    _ochain = chain


class ActiveMixin(_CoreMixin):

    def commit(self):
        '''consume call chain until exhausted'''
        self._outextend(
            c() for c in iterexcept(self._chain.popleft, IndexError)
        )
        return self

    _ocommit = commit


class LazyMixin(_CoreMixin):

    def commit(self):
        '''consume call chain until exhausted'''
        outgoing = deque(
            c() for c in iterexcept(self._chain.popleft, IndexError)
        )
        self.outgoing = outgoing
        return self

    _ocommit = commit


class RootedMixin(_CoreMixin):

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(RootedMixin, self).__init__(root)
        self._setup_chain()


class QMixin(_CoreMixin):

    '''chained queue mixin'''

    def clear(self):
        '''ANNIHILATE!!!'''
        self._oclear()
        self._cclear()
        return self

    _cclear = clear

    def tap(self, call, key=False):
        '''
        add call

        @param call: callable or appspace label
        @param key: linked call chain key (default: False)
        '''
        # reset postitional arguments
        self._args = ()
        # reset keyword arguments
        self._kw = {}
        # set current application
        self._call = self._M.get(call, key) if isstring(call) else call
        return self

    _ctap = tap


class _SubQMixin(RootedMixin, QMixin):

    '''linked call chain queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(_SubQMixin, self).__init__(root)
        # sync with root callable
        self._call = root._call
        # sync with root postitional arguments
        self._args = root._args
        # sync with root keyword arguments
        self._kw = root._kw


class ActiveRootedQMixin(_SubQMixin):

    '''active rooted queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(ActiveRootedQMixin, self).__init__(root)
        # sync with root incoming things
        self._inextend(root.incoming)
        # sync with root outgoing things
        self._outextend(root.outgoing)


class LazyRootedQMixin(_SubQMixin):

    '''lazy linked call chainlet queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(LazyRootedQMixin, self).__init__(root)
        # sync with root incoming things
        self.incoming = root.incoming
        # sync with root outgoing things
        self.outgoing = root.outgoing
