# -*- coding: utf-8 -*-
'''root mixins'''

from callchain.mixin.reset import ResetLocalMixin


class RootMixin(ResetLocalMixin):

    '''root chain mixin'''

    def __call__(self, *args):
        '''new chain session'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self.extend(args)
        return self

    _r_call = __call__

    def back(self, link):
        '''
        handle chainlet end

        @param link: linked chain
        '''
        self.clear()
        # extend call chain with root call chain
        self._cappend(link._chain)
        return self

    _rback = back


class EventRootMixin(RootMixin):

    '''root event mixin'''

    def _eventq(self, event):
        '''
        fetch linked call chain tied to `event`

        @param event: event label
        '''
        key = self.E.event(event)
        # fetch linked call chain bound to event
        queue = self.E.get(key)
        if queue is None:
            # create liked call chain if nonexistent
            queue = self._callchain
            self.E.on(key, queue)
        return queue

    _e_eventq = _eventq

    def _event(self, event):
        '''
        fetch calls bound to `event`

        @param event: event label
        '''
        return self.E.events(self.E.event(event))

    _e_event = _event

    def event(self, event):
        '''
        create or fetch `event`

        @param event: event label
        '''
        self.E.event(event)
        return self

    _eevent = event

    def unevent(self, event):
        '''
        drop `event`

        @param event: event label
        '''
        self.E.unevent(event)
        return self

    _eunevent = unevent
