# -*- coding: utf-8 -*-
'''call chains core'''

from collections import deque

from callchain.octopus import Octopus
from callchain.octopus.keys import NoServiceError

from callchain.chains.core import QueueMixin, LoneMixin

__all__ = ('ActiveChainQMixin', 'LazyChainQMixin', 'callchain')


class _ChainMixin(Octopus):

    '''call chain core mixin'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(_ChainMixin, self).__init__(pattern, required, defaults, **kw)
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
        self._cappend(link._chain)
        return self

    _oback = back

    def switch(self, label, key=False):
        '''
        overt switch to linked call chain from external appspace

        @param label: linked call chain label
        @param key: linked call chain chain key (default: False)
        '''
        return self.M.get(label, key)(self)

    _oswitch = switch


class callchain(_ChainMixin, LoneMixin):

    '''call chain'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(callchain, self).__init__(pattern, required, defaults, **kw)
        self.outgoing = deque()
        # outgoing things right extend
        self._outextend = self.outgoing.extend
        # outgoing things clear
        self._outclear = self.outgoing.clear


class _ChainQMixin(_ChainMixin, QueueMixin):

    '''call chain queue mixin'''

    def back(self, link):
        '''
        return from linked call chain

        @param link: linked call chain
        '''
        self._oback(link)
        # sync with link callable
        self._call = link._call
        # sync with link postitional arguments
        self._args = link._args
        # sync with link keyword arguments
        self._kw = link._kw
        return self

    _cback = back


class ActiveChainQMixin(_ChainQMixin):

    '''active call chain queue mixin'''

    def __call__(self, *args):
        '''load args into incoming thing'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self._inextend(args)
        return self

    def back(self, link):
        '''
        return from linked call chain

        @param link: linked call chain
        '''
        self._cback(link)
        # sync with link incoming things
        self._inclear()
        self._inextend(link.incoming)
        # sync with link outgoing things
        self._outclear()
        self._outextend(link.outgoing)
        return self

    _ccback = back


class LazyChainQMixin(_ChainQMixin):

    '''lazy call chain queue mixin'''

    def __call__(self, *args):
        '''load args into incoming thing'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self.incoming = iter([args[0]]) if len(args) == 1 else iter(args)
        return self

    def back(self, link):
        '''
        return from linked call chain

        @param link: linked call chain
        '''
        self._cback(link)
        # sync with link incoming things
        self.incoming = link.incoming
        # sync with link outgoing things
        self.outgoing = link.outgoing
        return self

    _ccback = back
