# -*- coding: utf-8 -*-
'''callchain call mixins'''

#from collections import deque
from itertools import chain, count
from functools import partial, total_ordering

from stuf import frozenstuf
from twoq.support import isstring
from appspace.builders import Appspace
from stuf.utils import OrderedDict, either, lazy, lazy_class

from callchain.managers import Events
from callchain.core import ConfigMixin
from callchain.patterns import Pathways
from callchain.compat import PriorityQueue
from callchain.keys.base import NoServiceError

###############################################################################
## chain components ###########################################################
###############################################################################


@total_ordering
class cury(object):

    __slots__ = ['_call', 'count']

    counter = count()

    def __init__(self, call, *args, **kw):
        self._call = partial(call, *args, **kw)
        self.count = next(self.counter)

    def __call__(self):
        return self._call()

    def __lt__(self, other):
        return self.count < other


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


class ChainMixin(ConfigMixin):

    '''chain mixin'''

    def __enter__(self):
        '''enter execution context'''
        return self

    def __exit__(self, e, t, b):
        '''exit execution context'''
        # invoke call chain
        self.commit()

    @either
    def L(self):
        '''local settings'''
        return self._M.localize(self) if self._M is not None else frozenstuf()

    @lazy_class
    def port(self):
        '''python 2.x <-> python 3.x porting helper'''
        from twoq.support import port
        return port

    @lazy
    def space(self):
        '''external appspace interface'''
        return Appspace(self.M) if self.M is not None else None

    def _setup(self, root):
        '''call chain setup'''
        # chain label
        self._CALLQ = '_chain'
        # call chain queue
        self._chain = PriorityQueue()

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
            # ...or lookup other appspaced thing
            return super(ChainMixin, self)._load(label)

    def chain(self, call, key=False, *args, **kw):
        '''
        add `call` or appspaced `call` to call chain, partializing it with any
        passed arguments

        @param call: call or appspaced call label
        @param key: appspace key (default: False)
        '''
        self._chain.put(cury(
            call, *(key,) + args, **kw) if not isstring(call) else cury(
            self.M.get(call, key), *args, **kw))
        return self

    def commit(self):
        '''consume call chain'''
        with self.ctx3():
            ln = self._chain.qsize()
            return self._xtend(
                c() for c in self.breakcount(self._chain.get, ln)
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
        return super(ChainMixin, self).tap(
            self._M.get(call, key) if isstring(call) else call
        )

    def wrap(self, call, key=False):
        '''build current callable from factory'''
        return super(ChainMixin, self).wrap(
            self._M.get(call, key) if isstring(call) else call
        )

#    def clear(self):
#        '''clear things'''
##        self._chain.clear()
#        return super(ChainMixin, self).clear()

    class Meta:
        pass


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
            #TODO: consider how this piles up
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
        with self.ctx1(workq='_work'):
            self.exhaustcall(
                lambda x: x(), self._xtend(self._events(*events))._iterable,
            )
            return self
        
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
