# -*- coding: utf-8 -*-
'''root chains'''

from appspace.keys import appifies

from callchain.services.apps import events
from callchain.internal import inside, einside
from callchain.keys.chain import KCallChain, KEventChain
from callchain.assembly.chain import CallChain, EventChain

from callchain.root.mixins import RootMixin
from callchain.root.apps import chain, event


@appifies(KCallChain)
@inside(chain)
class callchain(RootMixin, CallChain):

    '''root call chain'''


@appifies(KEventChain)
@einside(event, events)
class eventchain(RootMixin, EventChain):

    '''root event chain'''
