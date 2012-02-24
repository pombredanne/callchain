# -*- coding: utf-8 -*-
'''callchain call chain mixins'''

from twoq import twoq, port
from appspace.keys import appifies
from appspace.builders import Appspace
from stuf.utils import lazy, lazy_class

from callchain.core.paths import Pathways
from callchain.mixins.keys import ABranchChain, ARootChain

__all__ = ('ChainsQMixin', 'ChainQMixin', 'BranchQMixin')


class ChainsQMixin(twoq):

    '''base call chain'''

    @lazy
    def space(self):
        '''appspace'''
        return Appspace(self.M)

    def add(self, app, label, branch=False):
        '''
        add application to appspace

        @param app: new application
        @param label: application label
        @param branch: branch label (default: False)
        '''
        self.M.add(app, label, branch)
        return self

    def app(self, label, branch=False):
        '''
        fetch application in appspace

        @param label: application label
        @param branch: branch label (default: False)
        '''
        self._app = self.M.app(label, branch)
        return self

    def partial(self, call, branch=False, *args, **kw):
        '''
        partialize callable or appspaced application with any callable
        parameters

        @param call: callable or application label
        @param branch: branch label (default: False)
        '''
        self.M.partial(call, branch, *args, **kw)
        return self


@appifies(ABranchChain)
class BranchQMixin(ChainsQMixin):

    '''call chain branch'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(BranchQMixin, self).__init__()
        # root call chain
        self.root = root
        # application appspace
        self.M = root.M
        # manager settings
        self.L = root.L
        # sync with root
        self.extend(root.outgoing)


@appifies(ARootChain)
class ChainQMixin(ChainsQMixin):

    '''root call chain'''

    def __init__(self, pattern, required=None, defaults=None):
        '''
        init

        @param pattern: pattern configuration or appspace label
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(ChainQMixin, self).__init__()
        # application appspace
        self.M = Pathways.appspace(pattern, required, defaults)

    @property
    def settings(self):
        '''application settings'''
        return self.M.settings.final

    @lazy_class
    def port(self):
        '''python 2.x <-> python 3.x compatibility aid'''
        return port

    def branch(self, label, branch):
        '''
        add branch call chain class to root

        @param label: branch call chain class label
        @param branch: branch call chain class
        '''
        self.M.ez_register(ABranchChain, label, branch)
        return self
