# -*- coding: utf-8 -*-
'''event chain mixins'''

from itertools import chain

from stuf import orderedstuf
from appspace.keys import imap
from stuf.utils import iterexcept

from callchain.octopus.core import InsideMixin
from callchain.chains.mixins import LinkMixin, ChainMixin, BaseMixin

from callchain.events.registry import EventRegistry

__all__ = ('inside', 'EBaseMixin', 'EChainMixin', 'ELinkMixin')


class inside(InsideMixin):

    '''internal eventspace configuration'''

    def __init__(
        self, patterns=None, events=None, required=None, defaults=None, *args,
        **kw
    ):
        super(inside, self).__init__(patterns, required, defaults, *args, **kw)
        self.events = events

    def __call__(self, that):
        that._E = self.events.build()
        return self._ocall(that)


class EBaseMixin(BaseMixin):

    '''base event chain mixin'''

    ###########################################################################
    ## event listener management ##############################################
    ###########################################################################

    def on(self, event, call, key=False, *args, **kw):
        '''
        bind callable to event

        @param event: event label
        @param call: callable or eventspace label
        @param key: key label (default: False)
        '''
        self._eventq(event).chain(call, key, *args, **kw)
        return self

    def off(self, event):
        '''
        clear all callables bound to event

        @param event: event label
        '''
        self.E.unset(event)
        return self

    ###########################################################################
    ## event chain execution ##################################################
    ###########################################################################

    def _events(self, *events):
        '''get callables bound to `*events`'''
        getit = self._getevent
        return chain(*tuple(imap(getit, events)))

    def commit(self):
        '''run event chain'''
        try:
            # 1. before event
            self.trigger('before')
            # 2. work event
            self.trigger('work')
            # everything else
            super(EBaseMixin, self).commit()
            # 3. change event
            self.fire('change')
            # 4. any event
            self.fire('any')
            # 5. after event
            self.fire('after')
        except:
            # 6. problem event
            self.fire('problem')
        finally:
            # 7. event that runs irrespective
            self.fire('anyway')
        return self

    ###########################################################################
    ## event queue processing #################################################
    ###########################################################################

    def events(self, *events):
        '''
        ordered mapping of each event processing queue

        @param *events: event labels
        '''
        _eventq = self._eventq
        return orderedstuf((e, _eventq(e).queue) for e in events)

    def fire(self, *events):
        '''run callables bound to `*events` immediately'''
        try:
            # clear scratch queue
            self._sclear()
            # queue global and local bound callables
            self._sxtend(self._events(*events))
            # run event call chain until scratch queue is exhausted
            calls = iterexcept(self._scratch.popleft, IndexError)
            self.outappend(call() for call in calls)
        finally:
            # clear scratch queue
            self._sclear()
        return self

    def trigger(self, *events):
        '''add callables bound to `*events` to main call chain'''
        self._cxtend(self._events(*events))
        return self


class ELinkMixin(LinkMixin):

    '''linked event chain'''

    def __init__(self, root):
        '''
        init

        @param root: root event chain
        '''
        super(ELinkMixin, self).__init__(root)
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


class EChainMixin(ChainMixin):

    '''event chain'''

    def __init__(
        self, patterns=None, events=None, required=None, defaults=None, *args,
        **kw
    ):
        '''
        init

        @param patterns: pattern config or appspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(EChainMixin, self).__init__(
            patterns, required, defaults, *args, **kw
        )
        # local event registry
        self.E = events.build() if events is not None else None

    def _eventq(self, event):
        '''
        fetch call chain tied to `event`

        @param event: event label
        '''
        # fetch event
        event = self.event(event)
        # fetch linked call chain bound to event
        queue = self.E.get(event)
        if queue is None:
            # create linked call chain if nonexistent
            queue = self._chainlink(self)
            self.E.set(event, queue)
        return queue

    def _getevent(self, event):
        '''
        fetch callables bound to event

        @param event: event label
        '''
        return self.E.events(self._eget(event))

    def event(self, event):
        '''
        create or fetch event

        @param event: event label
        '''
        self.E.event(event)
        return self

    def unevent(self, event):
        '''
        drop event

        @param event: event label
        '''
        self.E.unevent(event)
        return self
