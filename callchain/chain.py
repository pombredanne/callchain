# -*- coding: utf-8 -*-
'''root chain mixins'''

from itertools import chain

from appspace.keys import NoAppError
from stuf.utils import lazy, lazy_class

from callchain.core import CoreMixin
from callchain.managers import Events
from callchain.patterns import Pathways
from callchain.core import ResetLocalMixin


class RootMixin(ResetLocalMixin):

    '''root chain mixin'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(RootMixin, self).__init__(pattern)
        if pattern is not None:
            # external appspace
            self.M = Pathways.appspace(pattern, required, defaults)
            # freeze external appspace global settings
            self.M.freeze(kw)
        else:
            self.M = None

    def __call__(self, *args):
        '''new chain session'''
        # clear call chain and queues and extend incoming things
        return self.clear().extend(args)

    @lazy_class
    def port(self):
        '''python 2.x <-> python 3.x porting helper'''
        from twoq.support import port
        return port

    def back(self, branch):
        '''
        handle switch from branch chain

        @param branch: branch chain
        '''
        self.clear()
        # sync with branch callable
        self._call = branch._call
        # sync with branch postitional arguments
        self._args = branch._args
        # sync with branch keyword arguments
        self._kw = branch._kw
        # sync with branch incoming and outgoing things
        return self.extend(branch.incoming).outextend(branch.outgoing)


class EventRootMixin(RootMixin):

    '''root event mixin'''

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

        @param patterns: pattern config or eventspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(EventRootMixin, self).__init__(
            patterns, required, defaults, *args, **kw
        )
        # update event registry with any other events
        if events is not None:
            self.E.update(events)

    def _eventq(self, event):
        '''
        linked chain bound to `event`

        @param event: event label
        '''
        key = self.E.event(event)
        # fetch linked chain bound to event
        queue = self.E.get(key)
        if queue is None:
            # create linked chain if nonexistent
            queue = self._linkedchain
            self.E.on(key, queue)
        return queue

    def _event(self, event):
        '''
        calls bound to `event`

        @param event: event label
        '''
        return self.E.events(self.E.event(event))

    def event(self, event):
        '''
        create or fetch `event`

        @param event: event label
        '''
        self.E.event(event)
        return self

    def unevent(self, event):
        '''
        drop `event`

        @param event: event label
        '''
        self.E.unevent(event)
        return self


class BranchMixin(ResetLocalMixin):

    ''''branch mixin'''

    def _setup(self, root):
        '''
        configure branch

        @param root: root chain
        '''
        super(BranchMixin, self)._setup(root)
        # root object
        self.root = root
        # root internal appspace manager
        self._M = root._M
        # root internal global settings
        self._G = root._G
        # root external appspace manager
        self.M = root.M


class EventBranchMixin(BranchMixin):

    '''event branch mixin'''

    @lazy
    def E(self):
        '''local event registry'''
        return Events('events')

    def _eventq(self, event):
        '''
        linked chain bound to `event`

        @param event: event label
        '''
        # fetch linked chain bound to event
        key = self.root.event(event)
        queue = self.E.get(key)
        if queue is None:
            # create linked chain if nonexistent
            queue = self._linkedchain
            self.E.on(key, queue)
        return queue

    def _event(self, event):
        '''
        calls bound to `event`

        @param event: event label
        '''
        key = self.root.event(event)
        return chain(self.E.events(key), self.root.E.events(key))


class BranchletMixin(CoreMixin):

    '''chainlet mixin'''

    def _setup(self, root):
        '''
        configure chainlet

        @param root: root chain
        '''
        super(BranchletMixin, self)._setup(root)
        # sync with root postitional arguments
        self._args = root._args
        # sync with root keyword arguments
        self._kw = root._kw
        # sync with root callable
        self._call = root._call
        # sync with root incoming things and outgoing things
        self.inclear().extend(root.incoming).outextend(root.outgoing)


class LinkedMixin(ResetLocalMixin):

    '''linked chain mixin'''

    def close(self):
        '''close out linked chain and switch to root chain'''
        return self.root.back(self)


class ChainletMixin(ResetLocalMixin):

    '''chainlet mixin'''

    def _load(self, label):
        '''
        silent internal switch back...

        @param label: appspaced thing label
        '''
        # fetch appspaced thing...
        try:
            return super(ChainletMixin, self)._load(label)
        # ...or revert to root chain
        except NoAppError:
            return getattr(self.back(), label)

    def _syncback(self, key, value):
        '''
        sync chainlet with root chain

        @param key: key of value
        @param value: value of value
        '''
        self.__dict__[key] = self.root.__dict__[key] = value

    def back(self):
        '''switch back to root chain'''
        return self.root.back(self)
