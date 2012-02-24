# -*- coding: utf-8 -*-
'''callchain events'''

from itertools import chain

from twoq.support import map
from appspace import Registry
from twoq import port, iterexcept
from stuf import orderedstuf, frozenstuf

from callchain.chains import chainq
from callchain.keys import AEvent, AChange, AAll, AInvoke, AProblem

__all__ = ['eventq', 'tripq']


class eventq(chainq):

    '''reacts to events'''

    def __init__(self, manager):
        '''
        init

        @param manager: manager
        '''
        super(eventq, self).__init__(manager)
        # populate system events
        ez_register = self.M.ez_register
        for k, v in port.items(self.L.EVENTS):
            ez_register(AEvent, k, v)

    ###########################################################################
    ## event lifecycle manager ################################################
    ###########################################################################

    def event(self, event):
        '''
        create or fetch event

        @param event: event label
        '''
        self.M.key(AEvent, event)
        return self

    def unevent(self, event):
        '''
        drop event

        @param event: event label
        '''
        self.M.unkey(AEvent, event)
        return self

    ###########################################################################
    ## event listener management ##############################################
    ###########################################################################

    def on(self, event, call, branch=False, *args, **kw):
        '''
        bind callable to event

        @param event: event label
        @param call: callable or application label
        @param branch: branch label (default: False)
        '''
        self.M.ez_subscribe(
            AEvent, event, self.M.partial(call, branch, *args, **kw),
        )
        return self

    def off(self, event):
        '''
        unbind all callables from event

        @param event: event label
        '''
        self.M.ez_unsubscribe(AEvent, event)
        return self

    ###########################################################################
    ## events #################################################################
    ###########################################################################

    class Meta:
        ## event names ########################################################
        # all event
        ALL = 'all'
        # change event
        CHANGE = 'change'
        # a problem
        PROBLEM = 'problem'
        # running chall chain event
        INVOKE = 'invoke'
        ## events #############################################################
        EVENTS = frozenstuf({
            ALL: AAll, CHANGE: AChange, INVOKE: AInvoke, PROBLEM: AProblem,
        })


class tripq(chainq):

    '''trips events'''

    def __init__(self, manager):
        '''
        init

        @param manager: manager
        '''
        super(tripq, self).__init__(manager)
        # local event registry
        self.E = Registry(key=AEvent)
        # event getter
        self._eget = self.M.event

    ###########################################################################
    ## event management #######################################################
    ###########################################################################

    def _eventq(self, event):
        '''
        get call chain tied to event

        @param event: event label
        '''
        # fetch global event
        event = self._eget(event)
        # fetch local event call chain
        queue = self.E.ez_lookup(AEvent, event)
        if queue is None:
            # create local event call chain if nonexistent
            queue = chainq(self.M, self.M.max_length)
            self.E.extend(AEvent, event, queue)
        return queue

    def bind(self, event, call, branch=False, *args, **kw):
        '''
        bind appspace application to local event call chain, partializing it
        with any parameters

        @param event: event label
        @param call: callable or application label
        @param branch: branch label (default: False)
        '''
        self._eventq(event).chain(call, branch, *args, **kw)
        return self

    ###########################################################################
    ## event chain execution ##################################################
    ###########################################################################

    def _getit(self, event):
        '''fetch callables bound to event'''
        e = self._eget(event)
        return chain(
            self.E.subscriptions(AEvent, e), self.M.subscriptions(AEvent, e),
        )

    def events(self, *events):
        '''get callables (global and local) bound to event'''
        getit = self._getit
        return chain(*(i for i in map(getit, events)))

    def fire(self, *events):
        '''invoke callables bound to events immediately'''
        try:
            # clear scratch queue
            self._sclear()
            # queue global and local bound callables
            self._sxtend(self.events(*events))
            # run event call chain until scratch queue is exhausted
            calls = iterexcept(self._scratch.popleft, IndexError)
            self.outappend(call() for call in calls)
        finally:
            # clear scratch queue
            self._sclear()
        return self

    def trigger(self, *events):
        '''add callables bound to events to primary call chain'''
        self._cxtend(self.events(*events))
        return self

    def commit(self):
        '''run call chain'''
        try:
            L = self.L
            self.trigger(L.INVOKE)
            self.trigger(L.ALL)
            self.trigger(L.CHANGE)
            super(tripq, self).commit()
        except:
            self.trigger(L.PROBLEM)
        return self

    ###########################################################################
    ## event queue processing #################################################
    ###########################################################################

    def event_queues(self, *events):
        '''
        ordered mapping of per event processing queue

        @param *events: event labels
        '''
        _eventq = self._eventq
        return orderedstuf((e, _eventq(e).queue) for e in events)
