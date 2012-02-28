# -*- coding: utf-8 -*-
'''callchain appconf'''

from appspace import Namespace

from callchain.core.paths import Pathways

__all__ = ['callchain']


class callchain(Pathways):

    class managers(Namespace):
        context = 'spine.contexts.managers.Manager'
        event = 'spine.events.managers.Manager'
        process = 'spine.processes.managers.Manager'
        workflow = 'spine.workflows.managers.Manager'

    class sessions(Namespace):
        context = 'spine.contexts.sessions.Session'
        event = 'spine.events.sessions.Session'
        process = 'spine.processes.sessions.Session'
        workflow = 'spine.workflows.sessions.Session'

    class workers(Namespace):
        context = 'spine.contexts.workers.Worker'
        event = 'spine.events.workers.Worker'
        process = 'spine.processes.workers.Worker'
        workflow = 'spine.workflows.workers.Worker'

    class things(Namespace):
        context = 'spine.contexts.things.Thing'
        event = 'spine.events.things.Thing'
        process = 'spine.processes.things.Thing'
        workflow = 'spine.workflows.things.Thing'

    class descriptors(Namespace):
        app = 'spine.bases.descriptors.app'
        call = 'spine.bases.descriptors.call'
        defer = 'spine.bases.descriptors.defer'
        extend = 'spine.bases.descriptors.extend'
        factory = 'spine.bases.descriptors.factory'
        method = 'spine.bases.descriptors.method'
        reextend = 'spine.bases.descriptors.reextend'
        refactory = 'spine.bases.descriptors.refactory'
        join = 'spine.bases.descriptors.join'
