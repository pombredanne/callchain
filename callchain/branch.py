# -*- coding: utf-8 -*-
'''callchain branch mixins'''

from itertools import chain

from stuf.utils import lazy
from appspace.keys import NoAppError

from callchain.managers import Events
from callchain.core import ResetLocalMixin, CoreMixin


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
