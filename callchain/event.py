# -*- coding: utf-8 -*-
'''callchain event chains'''

from callchain.chain import inside
from callchain.managers import Events

from callchain.mixins.core import EventMixin
from callchain.mixins.root import EventRootMixin
from callchain.mixins.call import EventCallMixin
from callchain.mixins.branch import (
    ChainletMixin, EventBranchMixin, LinkedMixin)


class einside(inside):

    '''internal eventspace configuration'''

    def __init__(
        self,
        patterns=None,
        events=None,
        required=None,
        defaults=None,
        *args,
        **kw
    ):
        '''
        init

        @param patterns: pattern config or appspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(einside, self).__init__(
            patterns, required, defaults, *args, **kw
        )
        self.events = events

    def __call__(self, that):
        that = super(einside, self).__call__(that)
        that.E = Events('events')
        that.E.update(self.events)
        return that


class Event(EventCallMixin, EventRootMixin, EventMixin):

    '''event chain'''


class EventLink(EventCallMixin, EventBranchMixin, EventMixin, LinkedMixin):

    '''linked event chain'''


class Eventlet(ChainletMixin, EventBranchMixin, EventMixin):

    '''eventlet'''
