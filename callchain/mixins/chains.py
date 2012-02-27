# -*- coding: utf-8 -*-
'''call chain mixins'''

from threading import local

from twoq import port
from appspace.builders import Appspace
from stuf.utils import lazy, lazy_class, either
from appspace.keys import appifies, AppLookupError, NoAppError

from callchain.core.paths import Pathways
from callchain.mixins.keys import ABranchChain, ARootChain

__all__ = ('ChainQMixin', 'LinkQMixin')


class ChainsQMixin(local):

    '''base call chain mixin'''

    def __getapp(self, label):
        try:
            item = self.M.get(label, self.M._current)
        except AppLookupError:
            try:
                # try finding namespace
                self.M.namespace(label)
            except AppLookupError:
                raise NoAppError(label)
            else:
                # temporarily swap primary label
                self.M._current = label
                return self
        else:
            # ensure current label is set back to default
            self.M._current = self.M._root
            return item

    @either
    def L(self):
        '''local manager settings'''
        return self.M.localize(self)

    @lazy
    def space(self):
        '''appspace'''
        return Appspace(self.M)

    def add(self, app, label, key=False):
        '''
        add application to appspace

        @param app: new application
        @param label: application label
        @param key: key label (default: False)
        '''
        self.M.set(label, app, key)
        return self

    def app(self, label, key=False):
        '''
        fetch application from appspace

        @param label: application label
        @param key: key label (default: False)
        '''
        self._call = self.M.get(label, key)
        return self


@appifies(ABranchChain)
class LinkQMixin(ChainsQMixin):

    '''liked call chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(LinkQMixin, self).__init__()
        # root call chain
        self.root = root
        # application appspace
        self.M = root.M
        # manager settings
        self.L = root.L

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            return self._getapp(label)


@appifies(ARootChain)
class ChainQMixin(ChainsQMixin):

    '''call chain mixin'''

    def __init__(self, pattern, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(ChainQMixin, self).__init__()
        # application appspace
        self.M = Pathways.appspace(pattern, required, defaults, ABranchChain)
        # freeze settings with any custom settings passed as keywords
        self.M.freeze(kw)

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            try:
                item = self.M.lookup1(ABranchChain, ABranchChain, label)
                if item is None:
                    raise NoAppError(label)
            except NoAppError:
                return self._getapp(label)
            else:
                return item(self)

    @property
    def settings(self):
        '''application settings'''
        return self.M.settings.final

    @lazy_class
    def port(self):
        '''python 2.x <-> python 3.x compatibility aid'''
        return port

    def link(self, label, branch):
        '''
        add linked call chain class

        @param label: linked call chain class label
        @param branch: linked call chain class
        '''
        self.M.ez_register(ABranchChain, label, branch)
        return self

    def switch(self, label):
        '''
        switch to linked call chain

        @param label: chain label
        '''
        return self.M.lookup1(ABranchChain, ABranchChain, label)
