# -*- coding: utf-8 -*-
'''queue mixins'''

from stuf.utils import iterexcept
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


class ContextMixin(ResetLocalMixin):

    '''base context manager'''

    def __init__(self, queue):
        '''
        init

        @param queue: queue
        '''
        super(ContextMixin, self).__init__(queue)
        self._cxtend = queue._cxtend
        self._cpopleft = queue._cpopleft

    @property
    def iterable(self):
        return iterexcept(self._cpopleft, IndexError)


class ActiveContext(ContextMixin):

    '''active context manager'''

    def __init__(self, queue):
        '''
        init

        @param queue: queue
        '''
        super(ActiveContext, self).__init__(queue)
        self._sxtend = queue._sxtend
        self._sappend = queue._sappend
        self._sclear = queue._sclear
        self._scratch = queue._scratch

    def __enter__(self):
        # clear scratch queue
        self._sclear()
        return self

    def __exit__(self, t, v, e):
        # extend callchain with scratch queue
        self._cxtend(self._scratch)
        # clear scratch queue
        self._sclear()

    def __call__(self, args):
        self._sxtend(args)

    def iter(self, args):
        self._sxtend(iter(args))

    def append(self, args):
        self._sappend(args)


class ActiveContextMixin(ResetLocalMixin):

    '''lazy context mixin'''

    @property
    def _callsync(self):
        return ActiveContext(self)


class LazyContext(ContextMixin):

    '''lazy context manager'''

    def __init__(self, queue):
        '''
        init

        @param queue: queue
        '''
        super(LazyContext, self).__init__(queue)
        self._queue = queue

    def __call__(self, args):
        self._queue._scratch = args

    def iter(self, args):
        self._queue._scratch = iter(args)

    def append(self, args):
        self._queue._scratch = iter([args])

    def __enter__(self):
        # clear scratch queue
        self._queue._scratch = None
        return self

    def __exit__(self, t, v, e):
        # extend incoming items with outgoing items
        self._cxtend(self._scratch)
        # clear scratch _queue
        self._queue._scratch = None


class LazyContextMixin(ResetLocalMixin):

    '''lazy context mixin'''

    @property
    def _callsync(self):
        return LazyContext(self)


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
