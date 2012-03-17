# -*- coding: utf-8 -*-
'''callchain rooted chain mixins'''

from itertools import chain

from appspace.keys import NoAppError

from callchain.managers import Events

from callchain.mixin.fluent import ResetLocalMixin


class RootletMixin(ResetLocalMixin):

    '''rootlet mixin'''

    def _load(self, label):
        '''
        silent internal switch back...

        @param label: appspaced thing label
        '''
        # fetch appspaced thing...
        try:
            return self._f_load(label)
        # ...or revert to root chain
        except NoAppError:
            return getattr(self.__rback(), label)

    _r_load = _load

    def _synchback(self, key, value):
        '''
        sync with back

        @param key: key of value
        @param value: value of value
        '''
        self.__dict__[key] = self.root.__dict__[key] = value

    def back(self):
        '''revert to root chain'''
        return self.root.back(self)

    _rback = __rback = back


class RootedMixin(ResetLocalMixin):

    ''''rooted chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(RootedMixin, self).__init__(root)
        self._setup(root)

    def _setup(self, root):
        '''
        setup chain

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


class EventRootedMixin(RootedMixin):

    '''rooted event chain mixin'''

    def _setup(self, root):
        '''
        init

        @param root: root event chain
        '''
        self._r_setup(root)
        # local event registry
        self.E = Events('events')

    _e_setup = _setup

    def _eventq(self, event):
        '''
        fetch linked call chain tied to ``event``

        @param event: event label
        '''
        # fetch linked call chain bound to event
        key = self.root.event(event)
        queue = self.E.get(key)
        if queue is None:
            # create liked call chain if nonexistent
            queue = self._callchain
            self.E.on(key, queue)
        return queue

    _e_eventq = _eventq

    def _event(self, event):
        '''
        fetch calls bound to ``event``

        @param event: event label
        '''
        key = self.root.event(event)
        return chain(self.E.events(key), self.root.E.events(key))

    _e_event = _event
