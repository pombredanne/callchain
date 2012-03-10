# -*- coding: utf-8 -*-
'''callchain rooted chain mixins'''

from itertools import chain

from appspace.keys import NoAppError

from callchain.managers import Events

from callchain.mixin.fluent import ResetLocalMixin


class RootedMixin(ResetLocalMixin):

    '''rooted mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root object
        '''
        super(RootedMixin, self).__init__(root)
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


class RootletMixin(ResetLocalMixin):

    def _load(self, label):
        '''
        silent internal switch back...

        @param label: appspaced thing label
        '''
        # fetch appspaced thing...
        try:
            return self._fload(label)
        # ...or revert to root chain
        except NoAppError:
            return getattr(self.back(), label)

    _rload = _load

    def back(self):
        '''revert to root chain'''
        return self.root.back(self)

    _rback = back


class RootedChainMixin(RootedMixin):

    ''''rooted chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(RootedChainMixin, self).__init__(root)
        self._setup_chain()


class ERootedChainMixin(RootedChainMixin):

    '''rooted event chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root event chain
        '''
        super(ERootedChainMixin, self).__init__(root)
        # local event registry
        self.E = Events('events')

    def _eventq(self, event):
        '''
        fetch linked call chain tied to `event`

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

    _eeventq = _eventq

    def _event(self, event):
        '''
        fetch calls bound to `event`

        @param event: event label
        '''
        key = self.root.event(event)
        return chain(self.E.events(key), self.root.E.events(key))

    _devent = _event
