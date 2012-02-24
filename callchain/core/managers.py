# -*- coding: utf-8 -*-
'''callchain managers'''

from functools import partial

from twoq import port
from stuf.utils import lazy
from appspace.managers import Manager as _Manager
from appspace.keys import AppLookupError, ConfigurationError

from callchain.core.keys import ASettings
from callchain.core.settings import Settings

__all__ = ['Manager']


class Manager(_Manager):

    '''appspace manager'''

    __slots__ = ('_key', '_label', '_ns', 'settings')

    def __init__(self, label='appconf', ns='default'):
        '''
        init

        @param label: label for application configuration object
        @param ns: label for internal namespace
        '''
        super(Manager, self).__init__(label, ns)
        self.ez_register(ASettings, ns, Settings)

    @property
    def _manage_class(self):
        '''manager class'''
        return Manager()

    @lazy
    def settings(self):
        '''get appspace settings'''
        return self.ez_lookup(ASettings, self._ns)()

    def add(self, app, label, branch=False):
        '''
        add application to appspace

        @param app: new application
        @param label: application label
        @param branch: branch label (default: False)
        '''
        manager = self.branch(branch) if branch else self
        # add to appspace
        return manager.set(label, app)

    def app(self, label, branch=False):
        '''
        fetch application in appspace

        @param label: application label
        @param branch: branch label (default: False)
        '''
        return self.get(branch).get(label) if branch else self.get(label)

    def apply(self, label, branch=False, *args, **kw):
        '''
        call application in appspace

        @param label: application label
        @param branch: branch label (default: False)
        '''
        return self.app(label, branch)(*args, **kw)

    def branch(self, label):
        '''
        add or fetch branch appspace

        @param label: label of appspace
        '''
        # fetch branch if exists...
        try:
            return self.get(label)
        # ...or create new branch
        except AppLookupError:
            return self.set(label, self._manage_class)
        raise ConfigurationError('invalid branch configuration')

    def partial(self, call, branch=False, *args, **kw):
        '''
        partialize callable or appspaced application with any callable
        parameters

        @param call: callable or application label
        @param branch: branch label (default: False)
        '''
        if port.isstring(call):
            return partial(self.apply, call, branch, *args, **kw)
        return partial(call, *args, **kw)
