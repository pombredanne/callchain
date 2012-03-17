# -*- coding: utf-8 -*-
'''queue mixins'''

from twoq.support import isstring

from callchain.mixin.reset import ResetLocalMixin


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
        @param key: linked call chain key (default: False)
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

    '''queued root chain mixin'''

    def back(self, link):
        '''
        handle return from linked call chain

        @param link: linked call chain
        '''
        self._rback(link)
        # sync with link callable
        self._call = link._call
        # sync with link postitional arguments
        self._args = link._args
        # sync with link keyword arguments
        self._kw = link._kw
        # sync with link incoming things
        self.extend(link.incoming)
        # sync with link outgoing things
        self.outextend(link.outgoing)
        return self

    _qback = back


class QRootedMixin(_QMixin):

    '''queued rooted chain mixin'''

    def _setup(self, root):
        '''
        setup chain

        @param root: root call chain
        '''
        super(QRootedMixin, self)._setup(root)
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
