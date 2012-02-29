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


class _ProcessMixin(local):

    '''base process chain mixin'''

    def __init__(self):
        super(_ProcessMixin, self).__init__()
        # process registry
        self.P = Registry('processes', PProcess)
        # populate system processes
        ez_register = self.P.ez_register
        exhaust(starmap(
            lambda x, y: ez_register(PProcess, x, y), items(self.L.PROCESSES),
        ))
    
    ###########################################################################
    ## process listener management ############################################
    ###########################################################################

    def batch(self, process, event, call, key=False, *args, **kw):
        '''
        bind appspace application to process call chain

        @param process: process label
        @param event: event label
        @param call: callable or application label
        @param key: key label (default: False)
        '''
        self._processq(process).on(event, call, key, *args, **kw)
        return self

    def unbatch(self, process):
        '''
        unbind all callables from a process

        @param process: process label
        @param event: event label
        '''
        self.P.ez_unsubscribe(PProcess, process)
        return self

    ###########################################################################
    ## process chain execution ################################################
    ###########################################################################

    def _processes(self, *processes):
        '''get callables bound to `*processes`'''
        fgetit = self._fgetit
        return chain(*(i for i in imap(fgetit, processes)))

    def commit(self):
        '''run process chain'''
        try:
            meta = self.L
            # trigger before events
            self.work(meta.BEFORE)
            # trigger work events
            self.work(meta.WORK)
            # trigger after events
            self.work(meta.AFTER)
            # run call chain
            super(_ProcessMixin, self).commit()
        except:
            # run abort events
            self.whip(meta.ABORT)
            # re-raise exception
            raise
        # run anyway events
        finally:
            self.whip(meta.ANYWAY)
        return self

    ###########################################################################
    ## process queue manipulation #############################################
    ###########################################################################

    def processes(self, *processes):
        '''ordered mapping of per `*processes` processing queues'''
        process = self._processq
        return orderedstuf((p, process(p)).eventqs for p in processes)
    
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


class ProcessLinkMixin(_ProcessMixin):
    
    '''linked process chain mixin'''
    
    def __init__(self, root):
        '''
        init

        @param root: root event chain
        '''
        super(ProcessLinkMixin, self).__init__(root)
        # root event chain getter
        self._reprocgetit = self.root._procgetit
        # process getter
        self._pget = self.M.process

    def _procgetit(self, process):
        # fetch global process
        process = self._pget(process)
        wsubscriptions = self.P.subscriptions
        for event in wsubscriptions([PProcess, EEvent], process):
            event.queue.trigger(event.name)
        return chain(
            wsubscriptions(PProcess, process),
            self._reprocgetit(PProcess, process),
        )


class ProcessChainMixin(_ProcessMixin):

    '''process chain'''

    def _procgetit(self, process):
        # fetch global process
        process = self._pget(process)
        wsubscriptions = self.P.subscriptions
        for event in wsubscriptions([PProcess, EEvent], process):
            event.queue.trigger(event.name)
        return chain(
            self.P.subscriptions(PProcess, process),
        )

    ###########################################################################
    ## process lifecycle management ###########################################
    ###########################################################################

    def process(self, process, *events):
        '''
        create or fetch process

        @param process: process label
        '''
        P = self.P
        this = P.ez_lookup(PProcess, process)
        if this is None:
            this = P.key(PProcess, process)
            subscriber = P.ez_subscribe
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
        self.P.unkey(PProcess, process)
        return self
