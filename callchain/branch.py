# -*- coding: utf-8 -*-
'''callchain branch mixins'''

from itertools import chain

from callchain.managers import Events
from callchain.resets import ResetLocalMixin


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
