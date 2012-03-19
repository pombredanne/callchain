# -*- coding: utf-8 -*-
'''fluent mixins'''

from itertools import chain
from collections import deque
from functools import partial

from stuf.utils import imap
from twoq.support import isstring
from appspace.keys import AppLookupError, NoAppError

from callchain.mixins.resets import ResetLocalMixin


class ChainMixin(ResetLocalMixin):

    '''chain mixin'''

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            return self._load(label)

    _c_getattr = __getattr__

    def _load(self, label):
        '''
        load thing from appspace

        @param label: label of appspaced thing
        '''
        _M = self._M
        try:
            # get appspace thing
            thing = _M.get(label, _M._current)
        except AppLookupError:
            try:
                # verify namespace
                _M.namespace(label)
            except AppLookupError:
                raise NoAppError(label)
            else:
                # temporarily swap current label
                _M._current = label
                return self
        else:
            # set current label back to root label
            _M._current = _M._root
            return thing

    _c_load = _load

    def _setup(self):
        '''configure chain'''
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
        # chain label
        self._callq = '_chain'

    _c_setup = _setup

    def chain(self, call, key=False, *args, **kw):
        '''
        add `call` or appspaced `call` to call chain, partializing it with any
        passed arguments

        @param call: call or appspaced call label
        @param key: appspace key (default: False)
        '''
        if not isstring(call):
            call = partial(call, *(key,) + args, **kw)
        else:
            call = partial(self.M.get(call, key), *args, **kw)
        self._cappend(call)
        return self

    _cchain = chain


class EventMixin(ChainMixin):

    '''event chain mixin'''

    @property
    def _callchain(self):
        '''new linked chain'''
        return self._M.get('chain', 'event')(self)

    def _events(self, *events):
        '''calls bound to `events`'''
        return chain(*tuple(imap(self._event, events)))

    _e_events = _events

    def on(self, event, call, key=False, *args, **kw):
        '''
        bind call to `event`

        @param event: event label
        @param call: label for call or eventspaced thing
        @param key: key label (default: False)
        '''
        self._eventq(event).chain(call, key, *args, **kw)
        return self

    _eon = on

    def off(self, event):
        '''
        clear calls bound to `event`

        @param event: event label
        '''
        self.E.unset(event)
        return self

    _eoff = off

    def trigger(self, *events):
        '''
        extend primary call chain with partials bound to `events`

        @param *events: event labels
        '''
        self._cxtend(self._events(*events))
        return self

    _etrigger = trigger


class QMixin(ResetLocalMixin):

    '''queued chain mixin'''

    def clear(self):
        '''clear queues'''
        self._oclear()
        self._cclear()
        return self

    _qclear = clear

    def tap(self, call, key=False):
        '''
        add call

        @param call: callable or appspace label
        @param key: link call chain key (default: False)
        '''
        # reset postitional arguments
        self._args = ()
        # reset keyword arguments
        self._kw = {}
        # set current application
        self._call = self._M.get(call, key) if isstring(call) else call
        return self

    _qtap = tap

    def swap(
        self, inq='incoming', outq='outgoing', tmpq='_scratch', callq='_chain',
    ):
        '''
        swap queues

        @param inq: incoming queue (default: 'incoming')
        @param outq: outcoming queue (default: 'outcoming')
        @param tmpq: temporary queue (default: '_scratch')
        @param callq: temporary queue (default: '_chain')
        '''
        self._inq = inq
        self._outq = outq
        self._tmpq = tmpq
        self._callq = callq
        return self
