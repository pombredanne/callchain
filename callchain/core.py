# -*- coding: utf-8 -*-
'''callchain core mixins'''

from itertools import chain
from collections import deque
from functools import partial

from stuf.utils import lazy
from twoq.support import isstring
from appspace.keys import AppLookupError, NoAppError

from callchain.managers import Events
from callchain.patterns import Pathways
from callchain.resets import ResetLocalMixin

###############################################################################
## chain components ###########################################################
###############################################################################


class inside(object):

    '''internal chain configuration'''

    def __init__(self, pattern, required=None, defaults=None, *args, **kw):
        '''
        init

        @param pattern: pattern configuration class or appspace label
        @param required: required global settings (default: None)
        @param defaults: default global settings (default: None)
        '''
        self.pattern = pattern
        self.required = required
        self.defaults = defaults
        self.args = args
        self.kw = kw

    def __call__(self, that):
        # internal appspace manager
        that._M = Pathways.appspace(
            self.pattern,
            self.required,
            self.defaults,
            *self.args,
            **self.kw
        )
        # lock internal appspace global settings
        that._M.settings.lock()
        # set internal appspace global settings
        that._G = that._M.settings.final
        return that


class ChainMixin(ResetLocalMixin):

    '''chain mixin'''

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


###############################################################################
## event chain components #####################################################
###############################################################################


class einside(inside):

    '''internal event chain configuration'''

    def __init__(
        self,
        patterns=None,
        events=None,
        required=None,
        defaults=None,
        *args,
        **kw
    ):
        '''
        init

        @param patterns: pattern config or appspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(einside, self).__init__(
            patterns, required, defaults, *args, **kw
        )
        self.events = events

    def __call__(self, that):
        that = super(einside, self).__call__(that)
        that.E = Events('events')
        that.E.update(self.events)
        return that


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
