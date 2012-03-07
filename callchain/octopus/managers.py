# -*- coding: utf-8 -*-
'''callchain octopus managers'''

from twoq import twoq
from stuf import stuf

from appspace.keys import AApp
from stuf.utils import bi, getcls, lazy
from appspace.managers import Manager as _Manager

from callchain.octopus.settings import Settings
from callchain.octopus.keys import ASettings, AService, NoServiceError

__all__ = ['Manager']


class Manager(_Manager):

    '''appspace manager'''

    __slots__ = ('_current', '_root', '_key', '_first', '_second')

    def __init__(self, label, key=AApp):
        '''
        init

        @param label: label for appspace
        @param key: default key for appspace (default: AApp)
        '''
        super(Manager, self).__init__(label, key)
        self.ez_register(ASettings, label, Settings)

    @lazy
    def settings(self):
        '''get appspace settings'''
        return self.ez_lookup(ASettings, self._root)()

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
        ).smash().pick('Meta').members().reup().wrap(stuf).map().invoke(
            'update', *args, **kw
        ).value()

    def freeze(self, *args, **kw):
        '''finalize settings'''
        # pass any arbitrary settings
        self.settings.update(*args, **kw)
        self.settings.lock()

    def service(self, label):
        '''
        fetch internal service

        @param label: service label
        '''
        service = self.lookup1(AService, AService, label)
        if service is None:
            raise NoServiceError(label)
        return service
