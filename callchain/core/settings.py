# -*- coding: utf-8 -*-
'''callchain settings'''

from inspect import isclass

from twoq import twoq, port
from stuf import frozenstuf, stuf
from appspace.keys import appifies
from stuf.utils import bi, deepget, getcls, lazy_set, setter

from callchain.core.resets import ResetLocalMixin
from callchain.core.keys import ADefaultSettings, ARequiredSettings, ASettings

__all__ = ('DefaultSettings', 'RequiredSettings', 'Settings')


def object_walk(this):
    '''
    transform classes within an object into stufs

    @param this: object
    '''
    this_stuf = dict()
    for k, v in port.items(vars(this)):
        if not k.startswith('_'):
            if isclass(v):
                this_stuf[k] = object_walk(v)
            else:
                this_stuf[k] = v
    return this_stuf


class lock_set(lazy_set):

    '''lazily assign attributes with a custom setter'''

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # check if settings are locked
        if instance._locked:
            return setter(instance, self.name, self.method(instance))
        return self.method(instance)


@appifies(ASettings)
class Settings(ResetLocalMixin):

    '''settings management'''

    def __init__(self):
        '''init'''
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

    def _update_default(self, settings):
        '''
        update default settings

        @param settings: new settings
        '''
        if ADefaultSettings.implementedBy(settings):
            self._default.update(object_walk(settings))
        else:
            raise TypeError('invalid default settings')

    def _update_required(self, settings):
        '''
        update required settings

        @param settings: new settings
        '''
        if ARequiredSettings.implementedBy(settings):
            self._required.update(object_walk(settings))
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
            if ADefaultSettings.implementedBy(value):
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
        if ARequiredSettings.implementedBy(value):
            self._required.clear()
            self._update_required(value)
        else:
            raise TypeError('invalid required settings')

    def get(self, key, default=None):
        '''
        get value from settings

        @param key: key in settings
        @param default: default value (default: None)
        '''
        return deepget(self._final, key, default)

    def lock(self):
        '''lock settings'''
        self._locked = True

    def freeze(self, *args, **kw):
        '''finalize settings'''
        # pass any arbitrary settings
        self.update(*args, **kw)
        self.lock()

    def update(self, *args, **kw):
        '''update end setting'''
        self._final.update(*args, **kw)

    @bi
    def localize(self, thing, *args, **kw):
        '''
        generate local settings for some thing

        @param thing: some thing with local settings
        '''
        # gather local settings from thing and its base classes, adding any
        # arbitrary settings
        return twoq(
            [type.mro(getcls(thing)), [thing]]
        ).flatten().pick('Meta').members().reup().wrap(stuf).map().invoke(
            'update', *args, **kw
        ).value()


@appifies(ADefaultSettings)
class DefaultSettings(object):

    '''default settings manager'''

    userspace = 'appspace'


@appifies(ARequiredSettings)
class RequiredSettings(object):

    '''required settings manager'''

    appspace = userspace = 'appspace'
