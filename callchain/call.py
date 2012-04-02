# -*- coding: utf-8 -*-
'''callchain call mixins'''

from functools import partial
from itertools import chain, count

from twoq.support import isstring
from appspace.builders import Appspace
from stuf.utils import OrderedDict, lazy

from callchain.managers import Events
from callchain.core import ConfigMixin
from callchain.patterns import Pathways
from callchain.keys import NoServiceError
from callchain.support import Empty, Queue, PriorityQueue, total_ordering


@total_ordering
class Partial(object):

    '''partial wrapper'''

    __slots__ = ('_call', 'count', '__call__')

    counter = count()

    def __init__(self, call, *args, **settings):
        self.__call__ = partial(call, *args, **settings)
        priority = settings.pop('priority', None)
        self.count = next(self.counter) if priority is None else priority

    def __lt__(self, other):
        return self.count < other


###############################################################################
## chain components ###########################################################
###############################################################################


class inside(object):

    '''internal chain configuration'''

    __slots__ = ('pattern', 'required', 'defaults', 'args', 'kw')

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


class CallMixin(ConfigMixin):

    '''chain mixin'''

    def __enter__(self):
        '''enter execution context'''
        return self

    def __exit__(self, e, t, b):
        '''exit execution context'''
        # invoke call chain
        self.commit()

    def _load(self, label):
        '''
        silent internal switch to...

        @param label: label of appspaced thing
        '''
        try:
            # look up internal appspaced linked call chain...
            _M = self._M
            key = _M.service(label)
            return getattr(_M.get(key, key)(self), label)
        except NoServiceError:
            # ...or lookup some other appspaced thing
            return super(CallMixin, self)._load(label)

    @lazy
    def space(self):
        '''external appspace interface'''
        return Appspace(self.M) if self.M is not None else None

    def _setup(self, root):
        '''call chain setup'''
        # call chain queue
        self._chain = self._queue()

    def chain(self, call, key=False, *args, **kw):
        '''
        add `call` or appspaced `call` to call chain, partializing it with any
        passed arguments

        @param call: call or appspaced call label
        @param key: appspace key (default: False)
        '''
        self._chain.put(
            Partial(call, *(key,) + args, **kw) if not isstring(call)
            else Partial(self.M.get(call, key), *args, **kw)
        )
        return self

    def commit(self):
        '''consume call chain'''
        with self.ctx3():
            return self._xtend(
                c() for c in self.iterexcept(self._chain.get_nowait, Empty)
            )

    def switch(self, label, key=False):
        '''
        overt switch to linked chain configured in external appspace

        @param label: linked chain label
        @param key: linked chain chain key (default: False)
        '''
        return self.M.get(label, key)(self)

    def tap(self, call, key=False):
        '''
        add call

        @param call: callable or appspace label
        @param key: link call chain key (default: False)
        '''
        return super(CallMixin, self).tap(
            self._M.get(call, key) if isstring(call) else call
        )

    def wrap(self, call, key=False):
        '''build current callable from factory'''
        return super(CallMixin, self).wrap(
            self._M.get(call, key) if isstring(call) else call
        )

    class Meta:
        pass


class PriorityMixin(CallMixin):

    '''chain mixin'''

    _queue = PriorityQueue

    def chain(self, call, key=False, *args, **kw):
        '''
        add `call` or appspaced `call` to call chain, partializing it with any
        passed arguments

        @param call: call or appspaced call label
        @param key: appspace key (default: False)
        '''
        self._chain.put(
            Partial(call, *(key,) + args, **kw)
            if not isstring(call)
            else Partial(self.M.get(call, key), *args, **kw)
        )
        return self


class ChainMixin(CallMixin):

    '''chain mixin'''

    _queue = Queue

    def chain(self, call, key=False, *args, **kw):
        '''
        add `call` or appspaced `call` to call chain, partializing it with any
        passed arguments

        @param call: call or appspaced call label
        @param key: appspace key (default: False)
        '''
        if not isstring(call):
            self._chain.put_nowait(self._partial(call, *(key,) + args, **kw))
        else:
            self._chain.put_nowait(
                self._partial(self.M.get(call, key), *args, **kw)
            )
        return self


###############################################################################
## event chain components #####################################################
###############################################################################


class einside(inside):

    '''internal event chain configuration'''

    __slots__ = ('pattern', 'required', 'defaults', 'args', 'kw', 'events')

    def __init__(
        self, patterns, events=None, required=None, defaults=None, *args, **kw
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

    def commit(self):
        '''run event chain'''
        fire = self.fire
        try:
            # 1. "before" event 2. "work" event
            fire('before', 'work')
            # everything else
            super(EventMixin, self).commit()
            # 3. "change" event 4. "any" event 5. "after" event
            fire('change', 'any', 'after')
        except:
            # 6. "problem" event
            fire('problem')
        finally:
            # 7. event that runs "anyway"
            return fire('anyway')

    def fire(self, *events):
        '''
        run calls bound to `events` **NOW**

        @param *events: event labels
        '''
        with self.ctx1(workq=self._WORKVAR):
            return self.exhaustcall(
                lambda x: x(), self._xtend(self._events(*events))._iterable,
            )

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

    def queues(self, *events):
        '''
        ordered mapping of processing queues for `events`

        @param *events: event labels
        '''
        return OrderedDict((e, self._eventq(e)) for e in events)
