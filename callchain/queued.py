# -*- coding: utf-8 -*-
'''queue mixins'''

from twoq.support import isstring

from callchain.resets import ResetLocalMixin


class _QMixin(ResetLocalMixin):

    '''queued chain mixin'''

    def clear(self):
        '''clear queues'''
        self._oclear()
        self._cclear()
        return self

    _qclear = clear

    def tap(self, call, key=False):
        '''
        add call

        @param call: callable or appspace label
        @param key: link call chain key (default: False)
        '''
        # reset postitional arguments
        self._args = ()
        # reset keyword arguments
        self._kw = {}
        # set current application
        self._call = self._M.get(call, key) if isstring(call) else call
        return self

    _qtap = tap


class QRootMixin(_QMixin):

    '''queued root mixin'''

    def back(self, branch):
        '''
        handle switch from branch chain

        @param branch: branch chain
        '''
        self._rback(branch)
        # sync with branch callable
        self._call = branch._call
        # sync with branch postitional arguments
        self._args = branch._args
        # sync with branch keyword arguments
        self._kw = branch._kw
        # sync with branch incoming things
        self.extend(branch.incoming)
        # sync with branch outgoing things
        self.outextend(branch.outgoing)
        return self

    _qback = back


class QBranchMixin(_QMixin):

    '''queued branch mixin'''

    def _setup(self, root):
        '''
        configure call chain

        @param root: root object
        '''
        super(QBranchMixin, self)._setup(root)
        # sync with root postitional arguments
        self._args = root._args
        # sync with root keyword arguments
        self._kw = root._kw
        # sync with root callable
        self._call = root._call
        # sync with root incoming things
        self.inclear()
        self.extend(root.incoming)
        # sync with root outgoing things
        self.outextend(root.outgoing)

    _q_setup = _setup
