# -*- coding: utf-8 -*-
'''chain mixins'''

from callchain.mixin.reset import ResetLocalMixin


class CRootMixin(ResetLocalMixin):

    '''root call chain mixin'''

    def __call__(self, *args):
        '''new chain session'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self.extend(args)
        return self

    _dcall = __call__

    def back(self, link):
        '''
        handle chainlet end

        @param link: linked call chain
        '''
        self.clear()
        # extend call chain with root call chain
        self._cappend(link._chain)
        self._qback(link)
        return self

    _rback = back


class ERootMixin(CRootMixin):

    '''root event chain mixin'''

    def _eventq(self, event):
        '''
        fetch linked call chain tied to `event`

        @param event: event label
        '''
        # fetch linked call chain bound to event
        key = self.E.event(event)
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
        return self.E.events(self.E.event(event))

    _devent = _event

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
