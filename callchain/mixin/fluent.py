# -*- coding: utf-8 -*-
'''fluent mixins'''

from itertools import chain
from collections import deque
from functools import partial

from stuf.utils import imap
from twoq.support import isstring
from appspace.keys import AppLookupError, NoAppError

from callchain.mixin.reset import ResetLocalMixin


class FluentMixin(ResetLocalMixin):

    '''fluent interface mixin'''

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            return self._load(label)

    _f_getattr = __getattr__

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

    _f_load = _load


class ChainMixin(FluentMixin):

    '''chain mixin'''

    def _setup(self):
        '''setup'''
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

    _c_setup = _setup

    def _incallsync(self):
        '''move callchain to incoming for processing'''
        self.outsync()
        self.inclear()
        self.extend(self._chain)

    _c_incallsync = _incallsync

    def _callinsync(self):
        '''move callchain to incoming for processing'''
        self._cclear()
        self._chain(self.incoming)
        self.sync()

    _c_callinsync = _callinsync

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

    '''event mixin'''

    @property
    def _callchain(self):
        '''new linked chain'''
        return self._M.get('callchain', 'event')(self)

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
