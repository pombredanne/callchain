# -*- coding: utf-8 -*-
'''call mixins'''

from twoq.support import port
from appspace.builders import Appspace
from stuf import frozenstuf, orderedstuf
from stuf.utils import lazy, lazy_class, either, iterexcept

from callchain.keys.octopus import NoServiceError

from callchain.mixin.reset import ResetLocalMixin


class CallMixin(ResetLocalMixin):

    '''call mixin'''

    def _load(self, label):
        '''
        silent internal switch to...

        @param label: appspaced thing label
        '''
        try:
            # look up internal appspaced linked call chain...
            _M = self._M
            key = _M.service(label)
            return getattr(_M.get(key, key)(self), label)
        except NoServiceError:
            # ...or lookup other appspaced thing
            return self._fload(label)

    _cload = _load

    @either
    def L(self):
        '''local settings'''
        return self._M.localize(self) if self._M is not None else frozenstuf()

    @lazy_class
    def port(self):
        '''python 2.x <-> python 3.x compatibility helper'''
        return port

    @lazy
    def space(self):
        '''external appspace interface'''
        return Appspace(self.M) if self.M is not None else None

    def commit(self):
        '''consume call chain until exhausted'''
        self.outextend(
            c() for c in iterexcept(self._chain.popleft, IndexError)
        )
        return self

    _ccommit = commit

    def switch(self, label, key=False):
        '''
        overt switch to linked call chain in external appspace

        @param label: linked call chain label
        @param key: linked call chain chain key (default: False)
        '''
        return self.M.get(label, key)(self)

    _cswitch = switch

    class Meta:
        pass


class ECallMixin(CallMixin):

    '''event chain execution mixin'''

    def commit(self):
        '''run event chain'''
        fire = self.fire
        try:
            # 1. before event  2. work event
            self.trigger('before', 'work')
            # everything else
            self._ccommit()
            # 3. change event 4. any event 5. after event
            fire('change', 'any', 'after')
        except:
            # 6. problem event
            fire('problem')
        finally:
            # 7. event that runs irrespective
            fire('anyway')
        return self

    _ecommit = commit

    def fire(self, *events):
        '''run calls bound to `events` NOW'''
        try:
            # clear scratch queue
            self._sclear()
            # queue global and local bound callables
            self._sxtend(self._events(*events))
            # run event call chain until scratch queue is exhausted
            self.outextend(call() for call in iterexcept(
                self._scratch.popleft, IndexError,
            ))
        finally:
            # clear scratch queue
            self._sclear()
        return self

    def queues(self, *events):
        '''
        ordered mapping of processing queues for `events`

        @param *events: event labels
        '''
        return orderedstuf((e, self._eventq(e).outgoing) for e in events)

    _equeues = queues
