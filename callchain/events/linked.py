# -*- coding: utf-8 -*-
'''active event chains'''

from itertools import chain

from callchain.chains.linked import (
    ActiveLinkedQMixin, LazyLinkedQMixin, chainlinked)

from callchain.events.core import ECoreMixin, EventRegistry

__all__ = ('ActiveELinkedQMixin', 'LazyELinkedQMixin', 'eventlinked')


class _ELinkedMixin(ECoreMixin):

    '''linked event chain'''

    def __init__(self, root):
        '''
        init

        @param root: root event chain
        '''
        super(_ELinkedMixin, self).__init__(root)
        # root event chain getter
        self._regetit = self.root._getevent
        # event getter
        self._eget = self.root.event
        # local event registry
        self.E = EventRegistry('events') if root.events is not None else None

    def _eventq(self, event):
        '''
        fetch chain tied to `event`

        @param event: event label
        '''
        # fetch event from root call chain
        event = self._eget(event)
        # fetch linked call chain bound to event
        queue = self.E.get(event)
        if queue is None:
            # create liked call chain if nonexistent
            queue = self._chainlink(self)
            self.E.set(event, queue)
        return queue

    def _getevent(self, event):
        '''
        fetch callables bound to event

        @param event: event label
        '''
        e = self._eget(event)
        return chain(self.E.events(e), self._regetit(e))


class eventlinked(_ELinkedMixin, chainlinked):

    '''linked event chain'''


class ActiveELinkedQMixin(_ELinkedMixin, ActiveLinkedQMixin):

    '''active linked event chain mixin'''


class LazyELinkedQMixin(_ELinkedMixin, LazyLinkedQMixin):

    '''lazy linked event chain mixin'''
