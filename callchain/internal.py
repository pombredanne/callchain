# -*- coding: utf-8 -*-
'''callchain internal configuration'''

from threading import local

from stuf.six import items
from stuf.utils import getcls, lazybase, exhaustmap

from callchain.managers import Events
from callchain.patterns import Pathways


class inside(object):

    '''internal appspace configuration'''

    def __init__(self, pattern, required=None, defaults=None, *args, **kw):
        '''
        init

        @param pattern: pattern configuration class or appspace label
        @param required: required global settings (default: None)
        @param defaults: default global settings (default: None)
        '''
        self.pattern = pattern
        self.required = required
        self.defaults = defaults
        self.args = args
        self.kw = kw

    def __call__(self, that):
        # internal appspace manager
        that._M = Pathways.appspace(
            self.pattern,
            self.required,
            self.defaults,
            *self.args,
            **self.kw
        )
        # lock internal appspace global settings
        that._M.settings.lock()
        # set internal appspace global settings
        that._G = that._M.settings.final
        return that

    _o_call = __call__


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
        that = self._o_call(that)
        that.E = Events('events')
        that.E.update(self.events)
        return that

    _e_call = __call__


class ResetTypeMixin(object):

    '''
    mixin to add ``reset`` method to descriptors inheriting from ``lazybase``
    '''

    def reset(self):
        '''reset previously accessed ``lazybase`` attributes'''
        this = vars(self)
        that = vars(getcls(self))
        t = lambda x, y: x in this and isinstance(y, lazybase)
        exhaustmap(items(that), delattr, t)

    _rreset = reset


class ResetLocalMixin(local):

    '''
    mixin to add ``reset`` method to descriptors inheriting from ``lazybase``
    (thread ``local`` version)
    '''

    def reset(self):
        '''reset previously accessed ``lazybase`` attributes'''
        this = vars(self)
        that = vars(getcls(self))
        t = lambda x, y: x in this and isinstance(y, lazybase)
        exhaustmap(items(that), delattr, t)

    _rreset = reset