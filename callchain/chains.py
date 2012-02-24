# -*- coding: utf-8 -*-
'''callchain chains'''

from collections import deque

from appspace.builders import Appspace
from twoq import twoq, port, iterexcept
from stuf.utils import lazy, lazy_class

from callchain.paths import Pathways

__all__ = ['chainq', 'leadq']


class chainq(twoq):

    '''call chain execution'''

    def __init__(self, manager, *args):
        '''
        init

        @param manager: appspace manager
        '''
        super(chainq, self).__init__()
        # application appspace
        self.M = manager
        # manager settings
        self.L = manager.L
        #######################################################################
        ## call chain #########################################################
        #######################################################################
        self._chain = deque()
        # call chain right extend
        self._cxtend = self._chain.extend
        # call chain right append
        self._cappendright = self._chain.append
        # call chain left append
        self._cappendleft = self._chain.appendleft
        # call chain left pop
        self._cpopleft = self._chain.popleft
        # call chain clear
        self._cclear = self._chain.clear

    @lazy
    def space(self):
        '''appspace'''
        return Appspace(self.M)

    def app(self, label, branch=False):
        '''
        fetch application in appspace

        @param label: application label
        @param branch: branch label (default: False)
        '''
        self._app = self.M.app(label, branch)
        return self

    def commit(self):
        '''invoke call chain'''
        # consume call chain until exhausted & put results in outgoing things
        calls = iterexcept(self._chain.popleft, IndexError)
        self.outappend(call() for call in calls)
        return self

    def add(self, app, label, branch=False):
        '''
        add application to appspace

        @param app: new application
        @param label: application label
        @param branch: branch label (default: False)
        '''
        self.M.add(app, label, branch)
        return self

    def chain(self, call, branch=False, *args, **kw):
        '''
        add callable to call chain, partialized with any parameters

        @param call: callable
        @param branch: branch label (default: False)
        '''
        self._cappendright(self.M.partial(call, branch, *args, **kw))
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


class leadq(chainq):

    '''call chain manager'''

    def __init__(self, pattern, required=None, defaults=None, *args):
        '''
        init

        @param pattern: pattern configuration or appspace label
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        # application appspace
        self.M = Pathways.appspace(pattern, required, defaults)
        super(leadq, self).__init__(self.M, *args)

    @property
    def settings(self):
        '''application settings'''
        return self.M.settings.final

    @lazy_class
    def port(self):
        '''python 2.x <-> python 3.x compatibility helper'''
        return port
