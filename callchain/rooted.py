# -*- coding: utf-8 -*-
'''callchain rooted chain mixins'''

from itertools import chain

from callchain.managers import Events
from callchain.call import ChainingMixin, QCallingMixin


class RootedMixin(ChainingMixin):

    '''rooted mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root object
        '''
        super(RootedMixin, self).__init__()
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


class RootedChainMixin(RootedMixin):

    ''''rooted chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(RootedChainMixin, self).__init__(root)
        self._setup_chain()


class RootedQMixin(RootedChainMixin, QCallingMixin):

    '''linked call chain queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(RootedQMixin, self).__init__(root)
        # sync with root postitional arguments
        self._args = root._args
        # sync with root keyword arguments
        self._kw = root._kw
        # sync with root callable
        self._call = root._call


class ERootedMixin(RootedChainMixin):

    '''rooted event chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root event chain
        '''
        super(ERootedMixin, self).__init__(root)
        # local event registry
        self.E = Events('events')

    def _eventq(self, event):
        '''
        fetch linked chain tied to `event`

        @param event: event label
        '''
        # fetch linked call chain bound to event
        key = self.root.event(event)
        queue = self.E.get(event)
        if queue is None:
            # create liked call chain if nonexistent
            queue = self._callchain(self)
            self.E.set(key, queue)
        return queue

    def _event(self, event):
        '''
        fetch calls bound to `event`

        @param event: event label
        '''
        key = self.root.event(event)
        return chain(self.E.events(key), self.root.E.events(key))
