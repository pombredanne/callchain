# -*- coding: utf-8 -*-
'''callchain settings management'''

from inspect import isclass

from stuf.six import items
from stuf import frozenstuf
from appspace.keys import appifies
from stuf.utils import deepget, lazy_set, setter

from callchain.mixins.resets import ResetLocalMixin
from callchain.keys.base import KDefaults, KRequired, KSettings

__all__ = ('DefaultSettings', 'RequiredSettings', 'Settings')


class lock_set(lazy_set):

    '''lazily assign attributes with a custom setter'''

    def __get__(self, this, that):
        if this is None:
            return self
        # check if settings are locked
        if this._locked:
            return setter(this, self.name, self.method(this))
        return self.method(this)


@appifies(KSettings)
class Settings(ResetLocalMixin):

    '''settings management'''

    def __init__(self):
        super(Settings, self).__init__()
        # default settings
        self._default = dict()
        # end settings
        self._final = dict()
        # required settings
        self._required = dict()
        # turn off lock initially
        self._locked = False

    def __repr__(self, *args, **kwargs):
        return str(self._final)

    @classmethod
    def _object_walk(cls, this):
        '''
        transform classes within an instance into a dictionary

        @param this: object
        '''
        this_stuf = dict()
        object_walk_ = cls._object_walk
        isclass_ = isclass
        for k, v in items(vars(this)):
            if not k.startswith('_'):
                if isclass_(v):
                    this_stuf[k] = object_walk_(v)
                else:
                    this_stuf[k] = v
        return this_stuf

    def _update_default(self, settings):
        '''
        update default settings

        @param settings: new settings
        '''
        if KDefaults.implementedBy(settings):
            self._default.update(self._object_walk(settings))
        else:
            raise TypeError('invalid default settings')

    def _update_required(self, settings):
        '''
        update required settings

        @param settings: new settings
        '''
        if KRequired.implementedBy(settings):
            self._required.update(self._object_walk(settings))
        else:
            raise TypeError('invalid required settings')

    @lock_set
    def defaults(self):
        '''get default settings separately'''
        return frozenstuf(self._default)

    @defaults.setter
    def defaults(self, value):
        '''
        set default settings separately

        @param value: default settings
        '''
        if value is not None:
            if KDefaults.implementedBy(value):
                self._default.clear()
                self._update_default(value)
            else:
                raise TypeError('invalid default settings')

    @lock_set
    def final(self):
        '''finalized settings'''
        end = self._default.copy()
        end.update(self._final.copy())
        end.update(self._required.copy())
        return frozenstuf(end)

    @lock_set
    def required(self):
        '''get required settings separately'''
        return frozenstuf(self._required)

    @required.setter
    def required(self, value):
        '''
        set required settings separately

        @param value: required settings
        '''
        if KRequired.implementedBy(value):
            self._required.clear()
            self._update_required(value)
        else:
            raise TypeError('invalid required settings')

    def get(self, key, default=None):
        '''
        value from settings

        @param key: key in settings
        @param default: default value (default: None)
        '''
        return deepget(self._final, key, default)

    def lock(self):
        '''lock settings'''
        self._locked = True

    def update(self, *args, **kw):
        '''update end setting'''
        self._final.update(*args, **kw)


@appifies(KDefaults)
class DefaultSettings(object):

    '''default settings manager'''

    userspace = 'appspace'


@appifies(KRequired)
class RequiredSettings(object):

    '''required settings manager'''

    appspace = userspace = 'appspace'
