# -*- coding: utf-8 -*-
'''callchain branch mixins'''

from itertools import chain

from callchain.managers import Events

from callchain.mixins.resets import ResetLocalMixin
from appspace.keys import NoAppError
from callchain.mixins.core import QMixin


class BranchMixin(ResetLocalMixin):

    ''''branch mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root object
        '''
        super(BranchMixin, self).__init__(root)
        self._setup(root)

    def _setup(self, root):
        '''
        configure branch

        @param root: root object
        '''
        self._c_setup()
        # root object
        self.root = root
        # root internal appspace manager
        self._M = root._M
        # root internal global settings
        self._G = root._G
        # root external appspace manager
        self.M = root.M
        # root external global settings
        self.G = root.G if self.M else None

    _r_setup = _setup


class EventBranchMixin(BranchMixin):

    '''event branch mixin'''

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
            queue = self._callchain
            self.E.on(key, queue)
        return queue

    _e_eventq = _eventq

    def _event(self, event):
        '''
        calls bound to `event`

        @param event: event label
        '''
        key = self.root.event(event)
        return chain(self.E.events(key), self.root.E.events(key))

    _e_event = _event

    def _setup(self, root):
        '''
        configure branch

        @param root: root object
        '''
        self._r_setup(root)
        # local event registry
        self.E = Events('events')

    _e_setup = _setup


class LitedMixin(ResetLocalMixin):

    '''lite branch chain mixin'''

    def _setup(self, root):
        '''
        configure branch

        @param root: root object
        '''
        self._d_setup()
        self._r_setup(root)


class LinkedMixin(ResetLocalMixin):

    '''linked chain mixin'''

    def close(self):
        '''close out linked chain and switch to root chain'''
        return self.root.back(self)

    _lclose = close


class ChainletMixin(ResetLocalMixin):

    '''chainlet base'''

    def _load(self, label):
        '''
        silent internal switch back...

        @param label: appspaced thing label
        '''
        # fetch appspaced thing...
        try:
            return self._c_load(label)
        # ...or revert to root chain
        except NoAppError:
            return getattr(self.__rback(), label)

    _r_load = _load

    def _syncback(self, key, value):
        '''
        sync chainlet with root chain

        @param key: key of value
        @param value: value of value
        '''
        self.__dict__[key] = self.root.__dict__[key] = value

    _r_syncback = _syncback

    def back(self):
        '''switch to root chain'''
        return self.root.back(self)

    _rback = __rback = back


class QBranchMixin(QMixin):

    '''queued branch mixin'''

    def _setup(self, root):
        '''
        configure call chain

        @param root: root object
        '''
        super(QBranchMixin, self)._setup(root)
        # sync with root postitional arguments
        self._args = root._args
        # sync with root keyword arguments
        self._kw = root._kw
        # sync with root callable
        self._call = root._call
        # sync with root incoming things
        self.inclear()
        self.extend(root.incoming)
        # sync with root outgoing things
        self.outextend(root.outgoing)

    _q_setup = _setup
