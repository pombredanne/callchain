# -*- coding: utf-8 -*-
'''process chain mixins'''

from threading import local
from itertools import chain, starmap

from stuf.six import items
from stuf.utils import exhaust
from stuf import orderedstuf, frozenstuf

from appspace import Registry
from twoq.support import map as imap
from callchain.mixins.events.events import EEvent

from callchain.mixins.processes.processes import (
    PAbort, PAfter, PAnyway, PBefore, PWork, PProcess)
from callchain.mixins.processes.events import (
    APrepare, ASync, ACreate, AModify, AExport, ADelete, AUpdate)


class ProcessMixin(local):

    '''manages local contexts, events, and processes'''

    def __init__(self, manager, max_length=None):
        '''
        init

        @param manager: global manager
        @param max_length: maximum queue length (default: None)
        '''
        super(ProcessMixin, self).__init__(manager, max_length)
        # process getter
        self._fget = self.M.process
        # process registry
        self.P = Registry('processes', PProcess)
        # populate system flows
        ez_register = self.P.ez_register
        exhaust(starmap(
            lambda x, y: ez_register(PProcess, x, y), items(self.L.PROCESSES),
        ))

    def batch(self, process, event, call, branch=False, *args, **kw):
        '''
        bind appspace application to process call chain

        @param process: process label
        @param event: event label
        @param call: callable or application label
        @param branch: branch label (default: False)
        '''
        self._processq(process).bind(event, call, branch, *args, **kw)
        return self

    def unbatch(self, process):
        '''
        unbind all callables from a process

        @param process: process label
        @param event: event label
        '''
        self.M.ez_unsubscribe(PProcess, process)

    ###########################################################################
    ## flow chain execution ###################################################
    ###########################################################################

    def commit(self):
        '''run call chain'''
        meta = self.L
        try:
            # trigger before events
            self.work(meta.BEFORE)
            # trigger work events
            self.work(meta.WORK)
            # trigger after events
            self.work(meta.AFTER)
            # run call chain
            super(ProcessMixin, self).commit()
        except:
            # run abort events
            self.whip(meta.ABORT)
            # re-raise exception
            raise
        # run anyway events
        finally:
            self.whip(meta.ANYWAY)
        return self

    def _fgetit(self, process):
        # fetch global process
        process = self._fget(process)
        wsubscriptions = self.P.subscriptions
        for event in wsubscriptions([PProcess, EEvent], process):
            event.queue.trigger(event.name)
        return chain(
            wsubscriptions(PProcess, process),
            self.M.subscriptions(PProcess, process),
        )

    def processes(self, *processes):
        '''get callables (global and local) bound to *processes'''
        fgetit = self._fgetit
        return chain(*(i for i in imap(fgetit, processes)))

    ###########################################################################
    ## process queue manipulation #############################################
    ###########################################################################

    def process_queues(self, *processes):
        '''ordered mapping of per *processes processing queues'''
        process = self._processq
        return orderedstuf((p, process(p)).eventqs for p in processes)


class ProcessChainMixin(ProcessMixin):

    '''manages global contexts, events, and processes'''

    def __init__(self, max_length=None):
        '''
        init

        @param max_length: maximum queue length (default: None)
        '''
        super(ProcessChainMixin, self).__init__(max_length)


    ###########################################################################
    ## global process lifecycle ###############################################
    ###########################################################################

    def process(self, process, *events):
        '''
        create or fetch process

        @param process: process label
        '''
        M = self.M
        this = M.ez_lookup(PProcess, process)
        if this is None:
            this = M.key(PProcess, process)
            subscriber = M.ez_subscribe
            ev = self.event
            for event in events:
                subscriber(
                    [PProcess, EEvent],
                    this,
                    frozenstuf(name=event, event=ev(event))
                )
        return this

    def unprocess(self, process):
        '''
        remove process

        @param process: process label
        '''
        self.M.unkey(PProcess, process)

    class Meta:
        ## process names ######################################################
        # something good
        INVOKE = 'invoke'
        # 1. first step
        BEFORE = 'before'
        # 2. second step
        WORK = 'work'
        # 3. third step
        AFTER = 'after'
        # 4. fourth step
        ANYWAY = 'anyway'
        # something bad
        ABORT = 'abort'
        ## process keys #######################################################
        PROCESSES = frozenstuf({
            BEFORE: PBefore,
            WORK: PWork,
            AFTER: PAfter,
            ANYWAY: PAnyway,
            ABORT: PAbort,
        })
        ## event names ########################################################
        # 1. preparation
        PREPARE = 'prepare'
        # 2. sending
        CREATE = 'create'
        UPDATE = 'modify'
        # 3. syncing
        SYNC = 'sync'
        # 4. manipulate
        UPDATE = 'update'
        DELETE = 'delete'
        # 5. exporting data
        EXPORT = 'export'
        ## event keys #########################################################
        EVENTS = frozenstuf({
            PREPARE: APrepare,
            SYNC: ASync,
            CREATE: ACreate,
            UPDATE: AModify,
            EXPORT: AExport,
            DELETE: ADelete,
            UPDATE: AUpdate,
        })
