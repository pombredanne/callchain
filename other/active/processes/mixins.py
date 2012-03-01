# -*- coding: utf-8 -*-
'''active process chain mixins'''

from threading import local

from stuf import frozenstuf
from stuf.utils import iterexcept

from callchain.events.services import EEvent

from callchain.mixins.processes.processes import PProcess


class _ProcessMixin(local):

    '''manages local contexts, events, and processes'''

    def whip(self, *processes):
        '''invoke callables bound to *processes immediately'''
        try:
            # clear scratch queue
            self._sclear()
            # queue global and local bound callables
            self._sxtend(self._processes(*processes))
            # run event call chain until scratch queue is exhausted
            calls = iterexcept(self._scratch.popleft, IndexError)
            self.outappend(call() for call in calls)
        finally:
            # clear scratch queue
            self._sclear()
        return self

    def work(self, *processes):
        '''add callables bound to *processes to primary call chain'''
        self._cxtend(self._processes(*processes))
        return self


class ProcessLinkMixin(local):

    '''manages local contexts, events, and processes'''

    def _processq(self, process):
        '''
        get call chain bound to process

        @param process: process label
        '''
        # fetch global process
        process = self._fget(process)
        # fetch local process call chain
        queue = self.P.ez_lookup(PProcess, process)
        if queue is None:
            # create local process call chain if nonexistent
            wsubscribe = self.P.process
            queue = _ProcessMixin(self.M, self.M.max_length)
            wsubscribe(PProcess, process, queue)
            qevent = queue.event
            for event in self.Q.subscriptions([PProcess, EEvent], process):
                name = event.name
                wsubscribe(
                    [PProcess, EEvent],
                    process,
                    frozenstuf(name=name, queue=qevent(event.name))
                )
        return queue


class ProcessChainMixin(_ProcessMixin):

    '''manages global contexts, events, and processes'''

    def _processq(self, process):
        '''
        get call chain bound to `process`

        @param process: process label
        '''
        # fetch global process
        process = self._fget(process)
        # fetch local process call chain
        queue = self.P.ez_lookup(PProcess, process)
        if queue is None:
            # create local process call chain if nonexistent
            wsubscribe = self.P.process
            queue = _ProcessMixin(self.M, self.M.max_length)
            wsubscribe(PProcess, process, queue)
            qevent = queue.event
            for event in self.Q.subscriptions([PProcess, EEvent], process):
                name = event.name
                wsubscribe(
                    [PProcess, EEvent],
                    process,
                    frozenstuf(name=name, queue=qevent(event.name))
                )
        return queue
