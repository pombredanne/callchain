# -*- coding: utf-8 -*-
'''call chains mixins'''

from collections import deque

from stuf.utils import iterexcept
from appspace.keys import NoAppError
from octopus.keys import NoServiceError
from octopus.resets import ResetLocalMixin
from octopus.core import Tentacle, Octopus

__all__ = ('BaseMixin', 'ChainMixin', 'LinkMixin')


class BaseMixin(ResetLocalMixin):

    '''chain base mixin'''

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
        @param key: key label (default: False)
        '''
        self._cappend(self.M.partial(call, key, *args, **kw))
        return self

    _ochain = chain


class LinkMixin(Tentacle):

    '''linked call chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(LinkMixin, self).__init__(root)
        self._setup_chain()
        # extend call chain with root call chain
        self._cxtend(root._chain)

    def _iget(self, label):
        '''
        silent internal switch back...

        @param label: appspaced thing label
        '''
        # fetch appspaced thing...
        try:
            return self._oiget(label)
        #...or return to root chain
        except NoAppError:
            return getattr(self.back(), label)

    _ciget = _iget

    def back(self):
        '''return to root call chain'''
        return self.root.back(self)

    _oback = back


class ChainMixin(Octopus):

    '''call chain base mixin'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(ChainMixin, self).__init__(pattern, required, defaults, **kw)
        self._setup_chain()

    def _iget(self, label):
        '''
        silent internal switch to...

        @param label: appspaced thing label
        '''
        try:
            # look up internally linked call chains...
            _M = self._M
            key = _M.service(label)
            return getattr(_M.get(key, key)(self), label)
        except NoServiceError:
            # ...or lookup other appspace things
            return self._oiget(label)

    _ciget = _iget

    def back(self, link):
        '''
        return from linked call chain

        @param link: linked call chain
        '''
        self.clear()
        # extend call chain with root call chain
        self._cxtend(link._chain)
        return self

    _oback = back

    def commit(self):
        '''
        consume call chain until exhausted
        '''
        self._rextend(
            call() for call in iterexcept(self._chain.popleft, IndexError)
        )
        return self

    _ocommit = commit

    def switch(self, label, key=False):
        '''
        overt switch to linked call chain from external appspace

        @param label: linked call chain label
        @param key: linked call chain chain key (default: False)
        '''
        return self.M.get(label, key)(self)

    _oswitch = switch
