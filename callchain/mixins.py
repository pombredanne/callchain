# -*- coding: utf-8 -*-
'''callchain mixins'''

from threading import local

from itertools import chain

from stuf.six import items
from stuf.utils import getcls, lazybase
from appspace.keys import imap, AppLookupError, NoAppError


class ResetTypeMixin(object):

    '''
    mixin to add a ".reset()" method to methods decorated with "lazybase"

    By default, lazy attributes, once computed, are static. If they happen to
    depend on other parts of an object and those parts change, their values may
    be out of sync.

    This class offers a ".reset()" method that an instance can call its state
    has _changed and invalidate all their lazy attributes. Once reset() is
    called, all lazy attributes are reset to original format and their accessor
    functions can be triggered again.
    '''

    def reset(self):
        '''reset accessed lazy attributes'''
        instdict = vars(self)
        classdict = vars(getcls(self))
        # To reset them, we simply remove them from the instance dict. At that
        # point, it's as if they had never been computed. On the next access,
        # the accessor function from the parent class will be called, simply
        # because that's how the python descriptor protocol works.
        for key, value in items(classdict):
            if all([key in instdict, isinstance(value, lazybase)]):
                delattr(self, key)


class ResetLocalMixin(local):

    '''thread `local` version versione of `ResetTypeMixin`'''

    def reset(self):
        '''reset previously accessed `lazybase` attributes'''
        instdict = vars(self)
        classdict = vars(getcls(self))
        for key, value in items(classdict):
            if all([key in instdict, isinstance(value, lazybase)]):
                delattr(self, key)


class ChainingMixin(ResetLocalMixin):

    '''chains mixin'''

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            return self._iget(label)

    def _iget(self, label):
        '''
        load item from appspace

        @param label: potential appspace label
        '''
        _M = self._M
        try:
            item = _M.get(label, _M._current)
        except AppLookupError:
            try:
                # lookup namespace
                _M.namespace(label)
            except AppLookupError:
                raise NoAppError(label)
            else:
                # temporarily swap primary label
                _M._current = label
                return self
        else:
            # ensure current label set back to default
            _M._current = _M._root
            return item

    _oiget = _iget


class EventsMixin(ChainingMixin):

    '''event chain mixin'''

    @property
    def _callchain(self):
        '''new linked event chain'''
        return self._M.get('callchain', 'event')(self)

    def _events(self, *events):
        '''get callables bound to `*events`'''
        return chain(*tuple(imap(self._event, events)))

    def on(self, event, call, key=False, *args, **kw):
        '''
        bind calls to `event`

        @param event: event label
        @param call: callable or eventspace label
        @param key: key label (default: False)
        '''
        self._eventq(event).chain(call, key, *args, **kw)
        return self

    def off(self, event):
        '''
        clear all calls bound to `event`

        @param event: event label
        '''
        self.E.unset(event)
        return self

    def trigger(self, *events):
        '''extend primary call chain with partials bound to `events`'''
        self._cxtend(self._events(*events))
        return self
