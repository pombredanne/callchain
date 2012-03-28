# -*- coding: utf-8 -*-
'''callchain core mixins'''

from itertools import chain
from collections import deque
from functools import partial

from stuf.utils import lazy
from twoq.support import isstring
from appspace.keys import AppLookupError, NoAppError

from callchain.mixins.resets import ResetLocalMixin


class ChainMixin(ResetLocalMixin):

    '''chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root chain
        '''
        super(ChainMixin, self).__init__()
        self._setup(root)

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            return self._load(label)

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

    @lazy
    def _chain(self):
        '''call chain queue'''
        return deque()

    def _setup(self, root):
        '''call chain setup'''
        # chain label
        self._CALLQ = '_chain'

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
        self._chain.append(call)
        return self

    def clear(self):
        '''clear things'''
        self._chain.clear()
        return super(ChainMixin, self).clear()

    def tap(self, call, key=False):
        '''
        add call

        @param call: callable or appspace label
        @param key: link call chain key (default: False)
        '''
        return super(ChainMixin, self).tap(
            self._M.get(call, key) if isstring(call) else call
        )

    def wrap(self, call, key=False):
        '''build current callable from factory'''
        return super(ChainMixin, self).wrap(
            self._M.get(call, key) if isstring(call) else call
        )


class EventMixin(ChainMixin):

    '''event chain mixin'''

    @property
    def _linkedchain(self):
        '''new linked chain'''
        return self._M.get('chain', 'event')(self)

    def _events(self, *events):
        '''calls bound to `events`'''
        return chain(*tuple(self._imap(self._event, events)))

    def on(self, event, call, key=False, *args, **kw):
        '''
        bind call to `event`

        @param event: event label
        @param call: label for call or eventspaced thing
        @param key: key label (default: False)
        '''
        self._eventq(event).chain(call, key, *args, **kw)
        return self

    def off(self, event):
        '''
        clear calls bound to `event`

        @param event: event label
        '''
        self.E.unset(event)
        return self

    def trigger(self, *events):
        '''
        extend primary call chain with partials bound to `events`

        @param *events: event labels
        '''
        self._chain.extend(self._events(*events))
        return self
