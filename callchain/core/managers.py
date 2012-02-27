# -*- coding: utf-8 -*-
'''callchain managers'''

from stuf.utils import lazy
from appspace.keys import AApp
from appspace.managers import Manager as _Manager

from callchain.core.keys import ASettings
from callchain.core.settings import Settings


__all__ = ['Manager']


class Manager(_Manager):

    '''appspace manager'''

    __slots__ = ('_current', '_root', '_key', '_ns', '_first', '_second')

    def __init__(self, label, key=AApp):
        '''
        init

        @param label: label for appspace
        @param key: default key for appspace (default: AApp)
        '''
        super(Manager, self).__init__(label, key)
        self.ez_register(ASettings, label, Settings)

    @property
    def _manage_class(self):
        '''manager class'''
        return Manager()

    @lazy
    def settings(self):
        '''get appspace settings'''
        return self.ez_lookup(ASettings, self._labels)()
