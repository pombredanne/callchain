# -*- coding: utf-8 -*-
'''callchain call mixins'''

from appspace.builders import Appspace
from stuf import frozenstuf, orderedstuf
from stuf.utils import either, iterexcept, lazy, lazy_class

from callchain.keys.core import NoServiceError

from callchain.mixins.resets import ResetLocalMixin


class CallMixin(ResetLocalMixin):

    '''chain execution mixin'''

    @either
    def L(self):
        '''local settings'''
        return self._M.localize(self) if self._M is not None else frozenstuf()

    @lazy_class
    def port(self):
        '''python 2.x <-> python 3.x porting helper'''
        from twoq.support import port
        return port

    @lazy
    def space(self):
        '''external appspace interface'''
        return Appspace(self.M) if self.M is not None else None

    def __enter__(self):
        '''enter context'''
        return self

    _c_enter = __enter__

    def __exit__(self, e, t, b):
        '''exit context'''
        # invoke call chain
        self.commit()

    _c_exit = __exit__

    def _load(self, label):
        '''
        silent internal switch to...

        @param label: label of appspaced thing
        '''
        try:
            # look up internal appspaced linked call chain...
            _M = self._M
            key = _M.service(label)
            return getattr(_M.get(key, key)(self), label)
        except NoServiceError:
            # ...or lookup other appspaced thing
            return self._c_load(label)

    _c_load = _load

    def switch(self, label, key=False):
        '''
        overt switch to linked chain configured in external appspace

        @param label: linked chain label
        @param key: linked chain chain key (default: False)
        '''
        return self.M.get(label, key)(self)

    _cswitch = switch

    def commit(self):
        '''consume call chain until exhausted'''
        self.outextend(c() for c in iterexcept(self._cpopleft, IndexError))
        return self

    _ccommit = commit

    class Meta:
        pass


class EventCallMixin(CallMixin):

    '''event execution mixin'''

    def commit(self):
        '''run event chain'''
        try:
            fire = self.fire
            # 1. "before" event then 2. "work" event
            self.trigger('before', 'work')
            # everything else
            self._ccommit()
            # 3. "change" event then 4. "any" event then 5. "after" event
            fire('change', 'any', 'after')
        except:
            # 6. "problem" event
            fire('problem')
        finally:
            # 7. event that runs irrespective and "anyway"
            fire('anyway')
        return self

    _ecommit = commit

    def fire(self, *events):
        '''
        run calls bound to `events` **NOW**

        @param events: event labels
        '''
        try:
            # clear scratch queue
            self._sclear()
            # queue global and local bound callables
            self._sxtend(self._events(*events))
            # run event call chain until scratch queue is exhausted
            self.outextend(c() for c in iterexcept(
                self._scratch.popleft, IndexError,
            ))
        finally:
            # clear scratch queue
            self._sclear()
        return self

    _efire = fire

    def queues(self, *events):
        '''
        ordered mapping of processing queues for `events`

        @param events: event labels
        '''
        return orderedstuf((e, self._eventq(e).outgoing) for e in events)

    _equeues = queues
